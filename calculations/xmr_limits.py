def calculate_xmr_limits(data, bound_upl=False, bound_lpl=True):

    mean = data.mean()

    moving_range = abs(data.diff())
    ave_mr = moving_range.mean()

    upl = mean + 2.660 * ave_mr
    lpl = mean - 2.660 * ave_mr
    url = 3.268 * ave_mr

    if bound_upl:
        upl = min(upl, 100)

    if bound_lpl:
        lpl = max(lpl, 0)

    return {
        "mean": mean,
        "moving_range": moving_range,
        "ave_mr": ave_mr,
        "UPL": upl,
        "LPL": lpl,
        "URL": url
    }