# components/charts.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    marker_size,
    figure_height,
    mean,
    UPL,
    LPL,
    URL,
    ave_mR,
    show_limits,
    rule_2,
    rule_3,
    line_mode
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
            mode=line_mode,
            cliponaxis=False,

            line=dict(
                color="steelblue",
                width=2
            ),

            marker=dict(
                size=marker_size,
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
            mode=line_mode,
            cliponaxis=False,

            line=dict(
                color="steelblue",
                width=2
            ),

            marker=dict(
                size=marker_size,#mr_sizes,
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

    return fig