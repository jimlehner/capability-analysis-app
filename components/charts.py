# components/charts.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy.stats import norm


from calculations.xmr_rules import apply_rule_2, apply_rule_3

from components.chart_styles import (
    get_x_marker_styles,
    get_mr_marker_styles
)


def build_empty_xmr_figure(figure_height):
    """
    Create an empty XmR figure skeleton (subplots + layout, no traces).

    Shared by create_xmr_chart and the stage-view code path so that
    both start from identical layout without duplicating traces.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    fig = make_subplots(
        rows=2,
        cols=1,
        vertical_spacing=0.05
    )

    fig.update_layout(
        height=figure_height,
        showlegend=False,
        margin=dict(t=25, b=0, r=20),
        xaxis2=dict(showticklabels=False),
        yaxis=dict(title="Individual Value (X)"),
        yaxis2=dict(title="Moving Range (mR)")
    )

    return fig


def create_xmr_chart(
    data,
    moving_range,
    figure_height,
    mean,
    UPL,
    LPL,
    URL,
    ave_mR,
    show_limits,
    show_annotations,
    rule_2,
    rule_3,
    marker_size,
    show_markers=True,
):
    """
    Create XmR chart figure.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    fig = build_empty_xmr_figure(figure_height)

    # -----------------------------
    # Apply detection rules
    # -----------------------------

    run_mask = (
        apply_rule_2(data, mean)
        if rule_2
        else [False] * len(data)
    )

    zone_mask = (
        apply_rule_3(data, UPL, LPL, mean)
        if rule_3
        else [False] * len(data)
    )


    # -----------------------------
    # Marker styles
    # -----------------------------

    x_colors, x_line_colors, x_sizes = get_x_marker_styles(
        data,
        UPL,
        LPL,
        run_mask,
        zone_mask,
        show_limits
    )


    mr_colors, mr_line_colors, mr_sizes = get_mr_marker_styles(
        moving_range,
        URL,
        show_limits
    )


    # -----------------------------
    # X Chart
    # -----------------------------

    fig.add_trace(
        go.Scatter(
            x=list(range(1, len(data)+1)),
            y=data,
            mode="lines+markers" if show_markers else "lines",
            cliponaxis=False,

            line=dict(
                color="steelblue",
                width=2
            ),

            marker=dict(
                size=marker_size,
                symbol="circle",
                color=x_colors,

                line=dict(
                    color=x_line_colors,
                    width=1 if show_limits else 0
                )
            )
        ),

        row=1,
        col=1
    )


    # -----------------------------
    # mR Chart
    # -----------------------------

    fig.add_trace(
        go.Scatter(
            x=list(range(2, len(moving_range)+2)),
            y=moving_range,
            mode="lines+markers" if show_markers else "lines",
            cliponaxis=False,

            line=dict(
                color="steelblue",
                width=2
            ),

            marker=dict(
                size=marker_size,
                symbol="circle",
                color=mr_colors,

                line=dict(
                    color=mr_line_colors,
                    width=1 if show_limits else 0
                )
            )
        ),

        row=2,
        col=1
    )

    if show_limits:
        # X chart limits
        fig.add_hline(
            y=UPL,
            line_dash="dash",
            line_color="red",
            row=1,
            col=1
        )

        fig.add_hline(
            y=LPL,
            line_dash="dash",
            line_color="red",
            row=1,
            col=1
        )

        # X chart center line
        fig.add_hline(
            y=mean,
            line_color="black",
            row=1,
            col=1
        )

        # Moving range chart upper limit
        fig.add_hline(
            y=URL,
            line_dash="dash",
            line_color="red",
            row=2,
            col=1
        )

        # mR chart center line
        fig.add_hline(
            y=ave_mR,
            line_color="black",
            row=2,
            col=1
        )

    if show_annotations:
        xchart_annotations = [
            ("UPL", UPL, "x", "y"),
            ("Mean", mean, "x", "y"),
            ("LPL", LPL, "x", "y"),
        ]

        mRchart_annotations = [
            ("URL", URL, "x2", "y2"),
            ("Ave. mR", ave_mR, "x2", "y2"),
        ]

        annotations = xchart_annotations + mRchart_annotations

        for label, y_value, x_ref, y_ref in annotations:
            fig.add_annotation(
                x=len(data),
                y=y_value,
                xref=x_ref,
                yref=y_ref,
                text=label,
                showarrow=False,
                xanchor="center",
                yanchor="middle",
                bgcolor="white",
                bordercolor="black",
                borderwidth=1,
                borderpad=2
            )


    fig.update_layout(
        margin=dict(t=0, b=0)
    )

    return fig

def build_empty_histogram_figure(figure_height):
    """
    Create an empty histogram figure skeleton
    (layout only, no traces).

    Returns
    -------
    plotly.graph_objects.Figure
    """

    fig = go.Figure()

    fig.update_layout(
        height=figure_height,
        showlegend=False,
        margin=dict(t=25, b=0, r=20),
        xaxis=dict(
            title="Individual Value (X)"
        ),
        yaxis=dict(
            title="Frequency"
        )
    )

    return fig

def build_process_histogram(data, 
                            USL, 
                            LSL, 
                            LPL, 
                            UPL, 
                            sigmax, 
                            histogram_bins, 
                            histogram_color,
                            highlight_outside_limits=False):

    # --- CALCULATIONS ---
    mean = data.mean()
    tolerance = USL - LSL
    target = LSL + (tolerance/2)

    # --- HISTOGRAM BINNING ---
    hist_counts, bin_edges = np.histogram(
        data,
        bins="auto"
    )

    bin_width = bin_edges[1] - bin_edges[0]

    # --- HISTOGRAM BAR COLORS ---

    # --- NORMAL DISTRIBUTION ---
    x = np.linspace(LPL, UPL, 500)

    pdf = norm.pdf(
        x,
        loc=mean,
        scale=sigmax
    )

    pdf_scaled = pdf * len(data) * bin_width

    # --- CREATE FIGURE ---
    fig_hist = go.Figure()

    # --- HISTOGRAM ---
    fig_hist.add_trace(
        go.Histogram(
            x=data,
            name="Process Performance",
            nbinsx=histogram_bins,
            # xbins=dict(
            #     start=bin_edges[0],
            #     end=bin_edges[-1],
            #     size=bin_width
            # ),
            marker=dict(
                color=histogram_color,
                line=dict(
                    color="white",
                    width=1
            )
        )
    )
    )

    # --- PROCESS POTENTIAL (NORMAL) DISTRIBUTION ---
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

    # --- PROCESS LIMITS & TARGET ---
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

    # --- LABELS ---
    labels = {
        "LSL": LSL,
        "USL": USL,
        "Target": target
    }

    # --- ADD ANNOTATIONS ---
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

        fig_hist.update_layout(
            width=600,
            height=425,
            margin=dict(
                l=20,
                r=20,
                t=30,
                b=0
            ),
            legend=dict(
                orientation="h",
                x=0.5,
                y=1.05,
                xanchor="center",
                yanchor="bottom"
            )
        )

    return fig_hist


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def build_capability_index_figure(ratios):

    ratios["y"] = 1

    fig = plt.figure(figsize=(15, 6))

    gs = fig.add_gridspec(4, 2)

    ax1 = fig.add_subplot(gs[0, 0])

    ax2 = fig.add_subplot(
        gs[1, 0],
        sharex=ax1
    )

    ax3 = fig.add_subplot(
        gs[2, 0],
        sharex=ax1
    )

    ax4 = fig.add_subplot(
        gs[3, 0],
        sharex=ax1
    )

    # Independent axis in second column
    ax5 = fig.add_subplot(gs[:, 1])

    palette = {
        "Capability": "tab:orange",
        "Performance": "#005a9c"
    }

    markers = {
        "Cp": "s",
        "Cpk": "o",
        "Pp": "s",
        "Ppk": "o"
    }

    # Cp vs Cpk
    sns.scatterplot(
        data=ratios[ratios["Parameter"].isin(["Cp", "Cpk"])],
        x="Value",
        y="y",
        hue="Group",
        style="Parameter",
        palette=palette,
        markers=markers,
        s=100,
        ax=ax1
    )

    ax1.get_legend().remove()

    # Pp vs Ppk
    sns.scatterplot(
        data=ratios[ratios["Parameter"].isin(["Pp", "Ppk"])],
        x="Value",
        y="y",
        hue="Group",
        style="Parameter",
        palette=palette,
        markers=markers,
        s=100,
        ax=ax2
    )

    ax2.get_legend().remove()

    # Cp vs Pp
    sns.scatterplot(
        data=ratios[ratios["Parameter"].isin(["Pp", "Cp"])],
        x="Value",
        y="y",
        hue="Group",
        style="Parameter",
        palette=palette,
        markers=markers,
        s=100,
        ax=ax3
    )

    ax3.get_legend().remove()

    # Cpk vs Ppk
    sns.scatterplot(
        data=ratios[ratios["Parameter"].isin(["Ppk", "Cpk"])],
        x="Value",
        y="y",
        hue="Group",
        style="Parameter",
        markers=markers,
        palette=palette,
        s=100,
        ax=ax4
    )

    ax4.get_legend().remove()

    # Capability vs Performance
    sns.scatterplot(
        data=ratios,
        x="Value",
        y="Value",
        hue="Group",
        palette=palette,
        style="Parameter",
        markers=markers,
        s=100,
        ax=ax5
    )

    # Label points
    labels = ratios.sort_values("Value").copy()

    last_value = None
    level = 0

    for _, row in labels.iterrows():

        if last_value is not None and abs(row["Value"] - last_value) < 0.15:
            level = 1 - level
        else:
            level = 0

        offset = 10 if level == 0 else -15

        ax5.annotate(
            row["Parameter"],
            (row["Value"], row["Value"]),
            xytext=(0, offset),
            textcoords="offset points",
            ha="center"
        )

        last_value = row["Value"]

    # Economic production zone
    ax5.axvline(1.5)
    ax5.axhline(1.5)

    ax5.annotate(
        "Zone of Economic Production",
        xy=(1.6, 1.6)
    )

    ax5.set_xlim(0, 3)
    ax5.set_ylim(0, 3)

    ax5.get_legend().remove()

    # Configuration
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_yticks([])
        ax.set_ylabel("")
        ax.set_xlabel("")

    ax4.set_xlabel("Process Capability Index Value")

    ax1.set_title("Cp vs Cpk")
    ax2.set_title("Pp vs Ppk")
    ax3.set_title("Cp vs Pp")
    ax4.set_title("Cpk vs Ppk")
    ax5.set_title("Capability vs Performance")

    sns.despine(fig=fig)

    fig.tight_layout()

    return fig