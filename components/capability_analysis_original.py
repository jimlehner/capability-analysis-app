import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm

from components.charts import (
    create_xmr_chart, 
    build_empty_xmr_figure,
    build_empty_histogram_figure
)

from components.chart_annotations import add_process_limit_lines, add_process_limit_annotations
from components.chart_stages import add_stage_traces, add_stage_boundaries, add_stage_labels

from calculations.capability_indices import (
    calculate_cp,
    calculate_cpk,
    calculate_pp,
    calculate_ppk
)
from calculations.xmr_limits import calculate_xmr_limits



URL = "https://raw.githubusercontent.com/jimlehner/broken-quality-initiative/refs/heads/main/data/shewharts-resistance-measurements.csv"

dataset = pd.read_csv(URL)

data = dataset["Resistance"]

# --- SPEC LIMITS AND TARGET ---
USL = 5295
LSL = 3395
tolerance = USL - LSL
target = LSL + (tolerance/2)

# --- CALCULATE PROCESS CAPABILITY INIDCES ---
Cp = calculate_cp(data, USL, LSL)
Cpk = calculate_cp(data, USL, LSL)
Pp = calculate_cp(data, USL, LSL)
Ppk = calculate_cp(data, USL, LSL)


def display_process_summary(LSL, USL, tolerance, target,
                            LPL, UPL, mean, ave_mR):

    st.markdown("#### Process Summary")

    st.markdown(
        "<hr style='margin: 0;'>",
        unsafe_allow_html=True
    )

    spec_col, stats_col = st.columns(2)

    with spec_col:
        st.write(f"**LSL:** {LSL:.2f}")
        st.write(f"**USL:** {USL:.2f}")
        st.write(f"**Tolerance:** {tolerance:.2f}")
        st.write(f"**Target:** {target:.2f}")

    with stats_col:
        st.write(f"**LPL:** {LPL:.2f}")
        st.write(f"**UPL:** {UPL:.2f}")
        st.write(f"**Mean:** {mean:.2f}")
        st.write(f"**Ave. mR:** {ave_mR:.2f}")

def display_capability_summary(characterization,
                               Cp, Cpk, Pp, Ppk):

    st.markdown("#### Process Capability")

    st.markdown(
        "<hr style='margin: 0;'>",
        unsafe_allow_html=True
    )

    st.write(f"**Characterization:** {LSL:.2f}")

    capability_col, performance_col = st.columns(2)

    with capability_col:
        st.write(f"**Cp:** {Cp:.2f}")
        st.write(f"**Cpk:** {Cpk:.2f}")

    with performance_col:
        st.write(f"**Pp:** {Pp:.2f}")
        st.write(f"**Ppk:** {Ppk:.2f}")
        

def display_capability_analysis():

    st.markdown("### Process Capability Analysis")
    data = dataset["Resistance"]
    mR = data.diff().abs()
    ave_mR = mR.mean()

    hist_fig_height = 500

    USL = 5295
    LSL = 3395
    tolerance = USL-LSL
    target = LSL + (tolerance/2)

    LPL = 3650.15
    UPL = 5346.21
    mean = 4498.18
    predictable_std = (UPL - LPL) / 6

    # --- PROCESS HISTOGRAM ---
    fig_hist = build_empty_histogram_figure(hist_fig_height)

    # ---------------------------------------------------------
    # Histogram binning
    # ---------------------------------------------------------

    hist_counts, bin_edges = np.histogram(
        data,
        bins="auto"
    )

    bin_width = bin_edges[1] - bin_edges[0]

    # ---------------------------------------------------------
    # Normal distribution
    # ---------------------------------------------------------

    x = np.linspace(LPL, UPL, 500)

    pdf = norm.pdf(
        x,
        loc=mean,
        scale=predictable_std
    )

    # Scale probability density to histogram frequency
    pdf_scaled = pdf * len(data) * bin_width


    # ---------------------------------------------------------
    # Create figure
    # ---------------------------------------------------------

    fig_hist = go.Figure()

    # ---------------------------------------------------------
    # Histogram
    # ---------------------------------------------------------

    fig_hist.add_trace(
        go.Histogram(
            x=data,
            name="Process Performance",
            xbins=dict(
                start=bin_edges[0],
                end=bin_edges[-1],
                size=bin_width
            ),
            marker=dict(
                color="#ADD8E6",
                line=dict(
                    color="white",
                    width=1
                )
            )
        )
    )

    # ---------------------------------------------------------
    # Normal distribution
    # ---------------------------------------------------------

    fig_hist.add_trace(
        go.Scatter(
            x=x,
            y=pdf_scaled,
            mode="lines",
            name="Process Potential",
            line=dict(
                color="#d72323",
                dash="dash",
                width=3
            )
        )
    )

    # --------------------------------------------------
    # Process limits and target
    # --------------------------------------------------
    parameters = [USL, LSL, target]

    for param in parameters:

        if param == target:
            color = "green"
            dash = "solid"
        else:
            color = "black"
            dash = "dash"

        fig_hist.add_vline(
            x=param,
            line_width=3,
            line_dash=dash,
            line_color=color
        )

    # --------------------------------------------------
    # Labels
    # --------------------------------------------------

    labels = {
        "LSL": LSL,
        "USL": USL,
        "Target": target
    }

    # Add annotations
    for text, x in labels.items():

        fig_hist.add_annotation(
            x=x,
            y=1,
            xref="x",
            yref="paper",
            text=text,
            showarrow=False,
            yanchor="bottom",
            bgcolor="white",
            bordercolor="black",
            borderwidth=0,
            borderpad=4
        )

# --------------------------------------------------
# Axis labels and layout
# --------------------------------------------------

    fig_hist.update_yaxes(
        title="Frequency",
        showgrid=True,
        gridcolor="white",
        gridwidth=1
    )

    fig_hist.update_xaxes(
        title="Resistance"
    )

    fig_hist.update_layout(
        width=600,
        height=500,
        legend=dict(
            orientation="h",
            x=0.5,
            y=1.05,
            xanchor="center",
            yanchor="bottom"
        )
    )

    # --------------------------------------------------
    # Results + Histogram
    # --------------------------------------------------

    results_col, histogram_col = st.columns([1, 3])

    with results_col:

        st.markdown("#### Process Summary")

        st.markdown(
            "<hr style='margin: 0;'>",
            unsafe_allow_html=True
        )

        spec_col, stats_col = st.columns(2)

        with spec_col:
            st.write(f"**LSL:** {LSL:.2f}")
            st.write(f"**USL:** {USL:.2f}")
            st.write(f"**Tolerance:** {tolerance:.2f}")
            st.write(f"**Target:** {target:.2f}")

        with stats_col:
            st.write(f"**LPL:** {UPL:.2f}")
            st.write(f"**UPL:** {LPL:.2f}")
            st.write(f"**Mean:** {mean:.2f}")
            st.write(f"**Ave. mR:** {ave_mR:.2f}")

        st.markdown("#### Process Capability")

        st.markdown(
                    "<hr style='margin: 0;'>",
                    unsafe_allow_html=True
                )

        st.write(f"**Characterization:**")

        capability_col, performance_col = st.columns(2)

        with capability_col:
            st.write(f"**Cp:** {USL:.2f}")
            st.write(f"**Cpk:** {LSL:.2f}")
        with performance_col:
            st.write(f"**Pp:** {target:.2f}")
            st.write(f"**Ppk:** {target:.2f}")

    with histogram_col:

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

    # # ==========================================
    # # XMR CHART
    # # ==========================================
    # # with col_xmr:

    # with st.expander("XmR Controls"):

    #     col4, col5, col6 = st.columns(3)

    #     tick_interval = col4.number_input(
    #         "Tick Interval (X)",
    #         min_value=1,
    #         step=1,
    #         key="tick_interval"
    #     )

    #     round_value = col5.number_input(
    #         "Number of Decimal Places",
    #         min_value=0,
    #         value=1,
    #         step=1,
    #         key="rounding_value"
    #     )

    #     tick_angle = col6.number_input(
    #         "X-Axis Tick Label Angle",
    #         min_value=0,
    #         value=0,
    #         step=15,
    #         key="tick_angle"
    #     )

    #     col7, col8, col9, col10, col11 = st.columns(5)

    #     show_limits = col7.checkbox(
    #         "Show Process Limits",
    #         value=True,
    #         key="show_limits"
    #     )

    #     show_annotations = col8.checkbox(
    #         "Show Annotations",
    #         value=True,
    #         key="show_annotations"
    #     )

    #     show_lines = col9.checkbox(
    #         "Show Connecting Lines",
    #         value=True,
    #         key="show_lines"
    #     )

    #     bound_UPL = col10.checkbox(
    #         "Bound UPL",
    #         value=False,
    #         key="bound_upl"
    #     )

    #     bound_LPL = col11.checkbox(
    #         "Bound LPL",
    #         value=True,
    #         key="bound_lpl"
    #     )

    #     col12, col13, col14, col15, spacer = st.columns(5)

    #     rule_2 = col12.checkbox(
    #         "Apply Detection Rule #2",
    #         value=False,
    #         key="rule_2"
    #     )

    #     rule_3 = col13.checkbox(
    #         "Apply Detection Rule #3",
    #         value=False,
    #         key="rule_3"
    #     )

    #     marker_size = col14.number_input(
    #         "Change marker size",
    #         min_value=0,
    #         max_value=15,
    #         value=8,
    #         step=1,
    #         key="marker_size"
    #     )

    #     figure_height = col15.number_input(
    #         "Change figure height",
    #         min_value=300,
    #         max_value=600,
    #         value=500,
    #         step=50,
    #         key="xmr_figure_height"
    #     )

    # # --- XMR CHART ---
    # fig_xmr = build_empty_xmr_figure(figure_height)
    # st.plotly_chart(fig_xmr, use_container_width=True)