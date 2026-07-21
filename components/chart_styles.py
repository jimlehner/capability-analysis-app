def point_color(v, in_run, in_zone, above_upl, below_lpl):
        if above_upl or below_lpl:
            return "#d72323"    # limit violation
        if in_run:
            return "#FFA500"    # run of 8+
        if in_zone:
            return "#18B007"    # 3 of 4 in outer zone
        return "steelblue"

"""
Chart styling utilities for XmR charts.

Contains:
- Point color assignment
- Marker color generation
- Marker size generation
- Marker line styling
"""

def point_color(v, in_run, in_zone, above_upl, below_lpl):
    """
    Assign marker color based on XmR chart conditions.

    Priority:
    1. Process limit violation
    2. Rule #2 violation (run of 8)
    3. Rule #3 violation (3 of 4 in outer zone)
    4. Normal point

    Parameters
    ----------
    v : float
        Data value (kept for compatibility)
    in_run : bool
        True if point satisfies Rule #2.
    in_zone : bool
        True if point satisfies Rule #3.
    above_upl : bool
        True if point exceeds upper process limit.
    below_lpl : bool
        True if point falls below lower process limit.

    Returns
    -------
    str
        Hex color or named color.
    """

    if above_upl or below_lpl:
        return "#d72323"      # limit violation

    if in_run:
        return "#FFA500"      # Rule #2: run of 8+

    if in_zone:
        return "#18B007"      # Rule #3: 3 of 4 in outer zone

    return "steelblue"


def get_x_marker_styles(
    data,
    UPL,
    LPL,
    run_mask,
    zone_mask,
    show_limits
):
    """
    Generate marker styles for the X chart.

    Returns
    -------
    tuple
        x_colors, x_line_colors, x_sizes
    """

    if not show_limits:

        return (
            ["steelblue"] * len(data),
            ["steelblue"] * len(data),
            [6] * len(data)
        )

    if LPL <= 0:

        x_colors = [
            point_color(
                v,
                run_mask[i],
                zone_mask[i],
                v > UPL,
                v <= 0
            )
            for i, v in enumerate(data)
        ]

        x_line_colors = [
            "black"
            if v > UPL or v <= 0 or run_mask[i] or zone_mask[i]
            else "steelblue"
            for i, v in enumerate(data)
        ]

        x_sizes = [
            7
            if v > UPL or v <= 0 or run_mask[i] or zone_mask[i]
            else 6
            for i, v in enumerate(data)
        ]

    else:

        x_colors = [
            point_color(
                v,
                run_mask[i],
                zone_mask[i],
                v > UPL,
                v < LPL
            )
            for i, v in enumerate(data)
        ]

        x_line_colors = [
            "black"
            if v > UPL or v < LPL or run_mask[i] or zone_mask[i]
            else "steelblue"
            for i, v in enumerate(data)
        ]

        x_sizes = [
            7
            if v > UPL or v < LPL or run_mask[i] or zone_mask[i]
            else 6
            for i, v in enumerate(data)
        ]

    return x_colors, x_line_colors, x_sizes


def get_mr_marker_styles(
    moving_range,
    URL,
    show_limits
):
    """
    Generate marker styles for the moving range chart.

    Returns
    -------
    tuple
        mr_colors, mr_line_colors, mr_sizes
    """

    if not show_limits:

        return (
            ["steelblue"] * len(moving_range),
            ["steelblue"] * len(moving_range),
            [6] * len(moving_range)
        )

    mr_colors = [
        "#d72323" if v > URL else "steelblue"
        for v in moving_range
    ]

    mr_line_colors = [
        "black" if v > URL else "steelblue"
        for v in moving_range
    ]

    mr_sizes = [
        7 if v > URL else 6
        for v in moving_range
    ]

    return mr_colors, mr_line_colors, mr_sizes


def get_default_marker_styles(data, moving_range):
    """
    Return default styles when process limits are hidden.
    """

    return {
        "x_colors": ["steelblue"] * len(data),
        "x_line_colors": ["steelblue"] * len(data),
        "x_sizes": [6] * len(data),
        "mr_colors": ["steelblue"] * len(moving_range),
        "mr_line_colors": ["steelblue"] * len(moving_range),
        "mr_sizes": [6] * len(moving_range)
    }
