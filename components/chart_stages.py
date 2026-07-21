"""
Stage handling for XmR charts.

Contains:
- Stage-specific trace generation
- Stage-specific limits
- Stage boundaries
- Stage labels
"""

import plotly.graph_objects as go

from calculations.xmr_rules import apply_rule_2, apply_rule_3

from components.chart_styles import (
    get_x_marker_styles,
    get_mr_marker_styles
)


def add_stage_traces(
    fig,
    data,
    stages,
    unique_stages,
    show_limits,
    rule_2,
    rule_3,
    line_mode
):
    """
    Add stage-specific X and mR traces.

    Each stage receives its own:
    - mean
    - UPL
    - LPL
    - URL
    - rule detection

    """

    for stage in unique_stages:

        stage_mask = stages == stage

        stage_data = (
            data[stage_mask]
            .reset_index(drop=True)
        )


        stage_x = [
            j + 1
            for j, m in enumerate(stage_mask)
            if m
        ]


        # -------------------------
        # Stage calculations
        # -------------------------

        stage_mean = stage_data.mean()

        stage_mR = abs(stage_data.diff())

        stage_ave_mR = stage_mR.mean()


        stage_UPL = (
            stage_mean +
            (2.660 * stage_ave_mR)
        )

        stage_LPL = max(
            0,
            stage_mean -
            (2.660 * stage_ave_mR)
        )

        stage_URL = (
            3.268 *
            stage_ave_mR
        )


        # -------------------------
        # Detection rules
        # -------------------------

        stage_run_mask = (
            apply_rule_2(
                list(stage_data),
                stage_mean
            )
            if rule_2
            else [False] * len(stage_data)
        )


        stage_zone_mask = (
            apply_rule_3(
                list(stage_data),
                stage_UPL,
                stage_LPL,
                stage_mean
            )
            if rule_3
            else [False] * len(stage_data)
        )


        # -------------------------
        # Marker styles
        # -------------------------

        s_colors, s_line_colors, s_sizes = get_x_marker_styles(
            stage_data,
            stage_UPL,
            stage_LPL,
            stage_run_mask,
            stage_zone_mask,
            show_limits
        )


        s_mr_colors, s_mr_line_colors, s_mr_sizes = get_mr_marker_styles(
            stage_mR,
            stage_URL,
            show_limits
        )


        # -------------------------
        # X chart trace
        # -------------------------

        fig.add_trace(
            go.Scatter(
                x=stage_x,
                y=stage_data,
                mode=line_mode,

                line=dict(
                    color="steelblue",
                    width=2
                ),

                marker=dict(
                    size=s_sizes,
                    color=s_colors,

                    line=dict(
                        color=s_line_colors,
                        width=1 if show_limits else 0
                    )
                )
            ),

            row=1,
            col=1
        )


        # -------------------------
        # mR chart trace
        # -------------------------

        fig.add_trace(
            go.Scatter(
                x=stage_x[1:],
                y=stage_mR[1:],
                mode=line_mode,

                line=dict(
                    color="steelblue",
                    width=2
                ),

                marker=dict(
                    size=s_mr_sizes[1:],
                    color=s_mr_colors[1:],

                    line=dict(
                        color=s_mr_line_colors[1:],
                        width=1 if show_limits else 0
                    )
                )
            ),

            row=2,
            col=1
        )


    return fig



def add_stage_boundaries(
    fig,
    stages
):
    """
    Add vertical lines between stages.
    """

    boundaries = [
        i
        for i in range(1, len(stages))
        if stages[i] != stages[i-1]
    ]


    for boundary in boundaries:

        fig.add_vline(
            x=boundary + 0.5,
            line_dash="solid",
            line_color="black",
            line_width=1,
            row="all",
            col=1
        )


    return fig



def add_stage_labels(
    fig,
    stages,
    unique_stages,
    custom_stage_labels,
    show_stage_labels
):
    """
    Add stage names above chart.
    """

    if not show_stage_labels:
        return fig


    for stage in unique_stages:

        stage_mask = stages == stage

        indices = [
            i
            for i, value in enumerate(stage_mask)
            if value
        ]


        midpoint = (
            indices[0] +
            indices[-1]
        ) / 2 + 1


        fig.add_annotation(
            xref="x",
            yref="paper",
            x=midpoint,
            y=1.05,

            text=f"<b>{custom_stage_labels[stage]}</b>",

            showarrow=False,

            font=dict(
                color="black",
                size=14
            ),

            xanchor="center"
        )


    return fig