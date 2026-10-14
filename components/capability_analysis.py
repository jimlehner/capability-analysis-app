import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm
from pathlib import Path

from components.dataset_selector import (
    render_upload_selectors,
    render_sample_selectors
)

from components.charts import (
    create_xmr_chart, 
    build_empty_xmr_figure,
    build_empty_histogram_figure,
    build_process_histogram,
    build_capability_index_figure
)

from components.chart_annotations import add_process_limit_lines, add_process_limit_annotations
from components.chart_stages import add_stage_traces, add_stage_boundaries, add_stage_labels

from calculations.capability_indices import (
    calculate_cp,
    calculate_cpk,
    calculate_pp,
    calculate_ppk
)

from calculations.characterize_process import characterize_process

from calculations.xmr_limits import calculate_xmr_limits

from data.loader import load_uploaded_dataset, load_sample_dataset, resolve_columns

from calculations.agresti_coull_interval_estimate import agresti_coull_interval_estimate


# --- DISPLAY CAPABILITY ANALYSIS ---
def display_capability_analysis(dataset_columns):

    # st.markdown("### Process Capability Analysis")

    # --- DATASET SELECTION ---
    st.markdown("#### Select a dataset or upload a CSV file")

    if "default_tick_interval" not in st.session_state:
            st.session_state.default_tick_interval = 5
    
    name_to_file = {v["name"]: k for k, v in dataset_columns.items()}

    col1, col2 = st.columns(2)
    
    with col1:
        selected_name = st.selectbox(
            "**Select a sample dataset**",
            ["None"] + list(name_to_file.keys()),
            key="sample_dataset"
        )

    with col2:
        uploaded_file = st.file_uploader(
            "**Upload your own dataset (CSV)**",
            type="csv",
            key="uploaded_csv"
        )

    # --- UPLOAD CSV PARAMETERS ---

    # Default value when using uploaded CSV
    selected_file = "None"

    # --- Warn if both sources are selected ---
    if uploaded_file is not None and selected_name != "None":
        st.warning(
            "A CSV file has already been uploaded. "
            "Please remove the uploaded file before selecting a sample dataset."
        )

        df = load_uploaded_dataset(uploaded_file)

    elif uploaded_file is not None:
        df = load_uploaded_dataset(uploaded_file)

    elif selected_name != "None":
        selected_file = name_to_file[selected_name]
        df = load_sample_dataset(selected_file, dataset_columns)

    else:
        df = None


    if df is None:
        st.info("To perform process capability analysis, select a dataset or upload a CSV.")
        return

    # --- COLUMN SELECTION ---
    if uploaded_file is not None:
        data_column, label_column, stage_column = render_upload_selectors(df)
    else:
        description = dataset_columns.get(selected_file, {}).get("description")
        st.divider()
        if description:
            st.markdown(
                f"### Selected dataset: <span style='color:#d72323'>{dataset_columns[selected_file]['name']}</span>",
                unsafe_allow_html=True
            )
            st.markdown(description)

        data_column, USL, LSL = render_sample_selectors(df, selected_file, dataset_columns)

    data = df[data_column].dropna()

    with st.expander("Numeric & Display Settings"):
        col_decimal, col_bins, col_hist_color = st.columns(3)

        with col_decimal:
            decimal_places = st.number_input(
                    "Decimal places",
                    min_value=0,
                    max_value=6,
                    value=2,
                    step=1
                )

        _, bin_edges = np.histogram(data, bins="auto")
        default_bins = len(bin_edges) - 1   

        with col_bins:
            histogram_bins = st.number_input(
                "Histogram Bins",
                min_value=1,
                max_value=100,
                value=default_bins,
                step=1
            )

        with col_hist_color:
            histogram_color = st.color_picker(
                "Histogram color",
                value="#ADD8E6"
            )

    # --- CALCULATIONS ---
    tolerance = USL - LSL
    target = LSL + (tolerance/2)

    xmr_results = calculate_xmr_limits(data)

    mean = xmr_results["mean"]
    LPL = xmr_results["LPL"]
    UPL = xmr_results["UPL"]
    URL = xmr_results["URL"]
    mR = xmr_results["moving_range"]
    ave_mR = xmr_results["ave_mr"]
    sigmax = ave_mR/1.128

    # --- CALCULATE AGRESTI COULL INTERVAL ESTIMATE ---
    AG_results = agresti_coull_interval_estimate(data, USL, LSL)

    n = AG_results["n"]
    Y = AG_results["Y"]
    p_hat = AG_results["p_hat"]
    p_tilde = AG_results["p_tilde"]
    AG_upper = min(1, AG_results["AG_upper"])
    AG_lower = max(0, AG_results["AG_lower"])

    # --- CALCULATE PROCESS CAPABILITY INIDCES ---
    Cp = calculate_cp(data, USL, LSL)["Cp"]
    Cpk = calculate_cpk(data, USL, LSL)["Cpk"]
    Pp = calculate_pp(data, USL, LSL)["Pp"]
    Ppk = calculate_ppk(data, USL, LSL)["Ppk"]

    characterization = characterize_process(data)

    col1, col2 = st.columns([1, 3])

    with col1:
        st.write("##### Characterization")
        st.markdown(
                        "<hr style='margin: 0;'>",
                        unsafe_allow_html=True
                    )

        if characterization == "Unpredictable":
            st.error(
                f"{characterization}. "
                "Use XmR chart to investigate the process for evidence of assignable causes of variation."
            )
        elif characterization == "Predictable":
            st.success(characterization)

        st.write("##### Process Summary")
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
            st.write(f"**UPL:** {LPL:.2f}")
            st.write(f"**LPL:** {UPL:.2f}")
            st.write(f"**Mean:** {mean:.2f}")
            st.write(f"**Ave. mR:** {ave_mR:.2f}")

        st.write("##### Process Capability Indices")

        st.markdown(
                "<hr style='margin: 0;'>",
                unsafe_allow_html=True
            )
            
        capability_col, performance_col = st.columns(2)
        
        with capability_col:
            st.write(f"**Cp:** {Cp:.{decimal_places}}")
            st.write(f"**Cpk:** {Cpk:.{decimal_places}}")
    
        with performance_col:
            st.write(f"**Pp:** {Pp:.{decimal_places}}")
            st.write(f"**Ppk:** {Ppk:.{decimal_places}}")

        st.write("#### Agresti-Coull Interval Estimate")
        st.markdown(
            "<hr style='margin-top: -20px; margin-bottom: -10px;'>",
            unsafe_allow_html=True
        )

        st.write(f"**Fraction Nonconforming:** {p_hat*100:.{decimal_places}f}%")
        st.write(f"**Biased Point Estimate:** {p_tilde*100:.{decimal_places}f}%")
        st.write(f"**Lower Interval Estimate:** {AG_lower*100:.{decimal_places}f}%")
        st.write(f"**Upper Interval Estimate:** {AG_upper*100:.{decimal_places}f}%")

    with col2:

        fig_hist = build_process_histogram(
            data,
            USL,
            LSL,
            LPL,
            UPL,
            sigmax,
            histogram_bins,
            histogram_color
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

        show_col1, show_col2, show_col3, show_col4 = st.columns(4)

        with show_col1:
            show_process_limits = st.checkbox(
                "Show process limits on XmR chart",
                value=True
            )
        with show_col2:
            show_annotations = st.checkbox(
                "Show XmR chart annotations",
                value=True
            )

        with show_col3:
            show_markers = st.toggle(
                "Show XmR chart markers",
                value=True
            )

        with show_col4:
            marker_size = st.slider(
                "Marker size",
                min_value=1,
                max_value=10,
                value=8,
                step=1
            )

        fig_xmrchart = create_xmr_chart(data, 
                                            mR, 
                                            300, 
                                            mean, 
                                            UPL, 
                                            LPL, URL, 
                                            ave_mR, 
                                            show_limits=show_process_limits,
                                            show_annotations=show_annotations,
                                            rule_2=False,
                                            rule_3=False,
                                            marker_size=marker_size, 
                                            show_markers=show_markers)
        
        st.plotly_chart(fig_xmrchart, use_container_width=True)

    with st.expander("Click here for an analysis summary"):
        st.write("#### Characterization")
        if characterization == "Unpredictable":
                st.write("With a characterization of UNPREDICTABLE, both common causes of routine variation " \
                "and assignable causes of exceptional variation influence process behavior. As such, " \
                "the process capability indicies are not an accurate measure of what the process has done in the past \
                    or what it can be made to do in the future. To improve this process " \
                "use the XmR chart to identify and eliminate the assignable causes.")
        else:
            st.write("With a characterization of PREDICTABLE, only common causes of routine variation influence " \
            "process behavior. As such, the performance indicies (Pp and Ppk) estimate what the process has " \
            "done in the past, while the capability indicies (CP and Cpk) estimate what it can be made to do in the future.")

        st.write("#### Process Capability Indices")

        st.write(f"As Cpk approaches Cp, and Ppk approach Pp, the process mean operates closer and closer to the target. \
                 Given a Cp of {round(Cp,2)} and Cpk of {round(Cpk,2)}, is the process mean operating near the target?")

        st.write(f"As a process is operated more predictably, the value of Pp will approach the value of Cp and the \
                 value of Ppk will approach the value of Cpk. When the two sets of values diverge, the process is not \
                 being operated predictably. Given a Pp of {round(Pp,2)} and Cp of {round(Cp,2)}, is the proces being operated \
                    predictably or unpredictably? Similarly, given a Ppk of {round(Cp,2)} and a Cpk of {round(Cpk,2)}, is \
                        the process being operated predictably?")

        st.write("#### Agresti-Coull Interval Estimate")
        st.write(f"The fraction nonconforming for this process is {p_hat*100}%. This empircal estimate has error bars that go \
                 down to {round(AG_lower*100,2)}% and up to {round(AG_upper*100,2)}%. This means that we can be reasonably certain \
                 that the lot fraction nonconforming is no more than {round(AG_upper*100,2)}% and also that it is likely greater \
                 than {round(AG_lower*100,2)}%.")

        st.write(f"If knowing that there is more than {round(AG_lower*100,2)}% nonconforming in the lot is bad enough, \
                 reject the lot. If knowing that there is less than {round(AG_upper*100,2)}% nonconforming \
                    is good enough, accept the lot. If {round(AG_lower*100,2)}% is not bad enough to reject the lot or if \
                        {round(AG_upper*100,2)}% is not good enough to accept the lot, then you do not have sufficient evidence \
                            to take either action. This is the truth about acceptance sampling. By forcing the acceptance or \
                                rejection of each lot, it leads to actions that are not always justified and may be detrimental. \
                                    The interval estimate tells us what we know AND what we do not know.")

    ratios = pd.DataFrame({
        "Group":["Capability", "Capability", "Performance", "Performance"],
        "Parameter":["Cp", "Cpk", "Pp", "Ppk"],
        "Value":[Cp, Cpk, Pp, Ppk]
    })