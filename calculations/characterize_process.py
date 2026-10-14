from calculations.xmr_limits import calculate_xmr_limits

def characterize_process(data):

    mR = data.diff().abs()

    xmr_results = calculate_xmr_limits(data)

    mean = xmr_results["mean"]
    LPL = xmr_results["LPL"]
    UPL = xmr_results["UPL"]
    URL = xmr_results["URL"]

    unpredictable = (
        (data > UPL).any()
        or
        (data < LPL).any()
        or
        (mR > URL).any()
    )

    if unpredictable:
        return "Unpredictable"

    return "Predictable"