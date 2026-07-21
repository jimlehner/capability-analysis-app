"""
Plotly annotation utilities for XmR charts.

Contains:
- Process limit horizontal lines
- Process limit annotations
- Stage boundary lines
- Stage title annotations
"""


def add_process_limit_lines(
    fig,
    mean,
    UPL,
    LPL,
    ave_mR,
    URL,
    show_limits
):
    """
    Add global XmR process limit lines.

    X chart:
        - Mean
        - UPL
        - LPL

    mR chart:
        - Average moving range
        - URL
    """

    if not show_limits:
        return fig

    hlines = [
        {
            "y": mean,
            "line_dash": "solid",
            "line_color": "black",
            "row": 1
        },
        {
            "y": UPL,
            "line_dash": "dash",
            "line_color": "#d72323",
            "row": 1
        },
        {
            "y": LPL,
            "line_dash": "dash",
            "line_color": "#d72323",
            "row": 1
        },
        {
            "y": URL,
            "line_dash": "dash",
            "line_color": "#d72323",
            "row": 2
        },
        {
            "y": ave_mR,
            "line_dash": "solid",
            "line_color": "black",
            "row": 2
        },
    ]

    for line in hlines:

        fig.add_hline(
            y=line["y"],
            line_dash=line["line_dash"],
            line_color=line["line_color"],
            line_width=2,
            row=line["row"],
            col=1
        )

    return fig


def add_process_limit_annotations(
    fig,
    mean,
    UPL,
    LPL,
    ave_mR,
    URL,
    round_value,
    show_annotations
):
    """
    Add XmR limit labels on right side of chart.
    """

    if not show_annotations:
        return fig


    annotations = [
        {
            "y": mean,
            "text": f"X̄: {mean:.{round_value}f}",
            "yref": "y1",
            "borderpad": 1
        },
        {
            "y": UPL,
            "text": f"UPL: {UPL:.{round_value}f}",
            "yref": "y1",
            "borderpad": 1
        },
        {
            "y": LPL,
            "text": f"LPL: {LPL:.{round_value}f}",
            "yref": "y1",
            "borderpad": 1
        },
        {
            "y": ave_mR,
            "text": f"<span style='text-decoration:overline'>mR</span>: {ave_mR:.{round_value}f}",
            "yref": "y2",
            "borderpad": 4.1
        },
        {
            "y": URL,
            "text": f"URL: {URL:.{round_value}f}",
            "yref": "y2",
            "borderpad": 1
        },
    ]


    for ann in annotations:

        fig.add_annotation(
            xref="paper",
            yref=ann["yref"],
            x=1,
            y=ann["y"],
            text=ann["text"],
            showarrow=False,
            font=dict(
                color="black",
                size=16
            ),
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            borderpad=ann["borderpad"],
            xanchor="right",
            yanchor="middle"
        )

    return fig


def add_stage_boundaries(
    fig,
    stages
):
    """
    Add vertical lines separating stages.
    """

    stage_boundaries = [
        i
        for i in range(1, len(stages))
        if stages[i] != stages[i-1]
    ]

    for boundary in stage_boundaries:

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

        stage_indices = [
            j
            for j, m in enumerate(stage_mask)
            if m
        ]

        x_mid = (
            stage_indices[0] +
            stage_indices[-1]
        ) / 2 + 1


        fig.add_annotation(
            xref="x",
            yref="paper",
            x=x_mid,
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