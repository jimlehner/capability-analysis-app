# Capability Ratio
def calculate_cp(data, USL, LSL):

    tolerance = USL - LSL

    mean = data.mean()

    stdev = data.std()

    moving_range = abs(data.diff())
    ave_mr = moving_range.mean()

    d2 = 1.128

    sigmax = ave_mr/d2

    cp = tolerance/(6*sigmax)

    return {
        "Cp": cp,
    }

# Centered Capability Ratio
def calculate_cpk(data, USL, LSL):

    tolerance = USL - LSL

    mean = data.mean()

    stdev = data.std()

    DNS = min(mean - LSL, USL - mean)

    moving_range = abs(data.diff())
    ave_mr = moving_range.mean()

    d2 = 1.128

    sigmax = ave_mr/d2

    cpk = DNS/(3*sigmax)

    return {
        "Cpk": cpk,
    }

# Performance Ratio
def calculate_pp(data, USL, LSL):

    tolerance = USL - LSL

    mean = data.mean()

    stdev = data.std()

    pp = tolerance/(6*stdev)

    return {
        "Pp": pp,
    }

# Centered Performance Ratio
def calculate_ppk(data, USL, LSL):

    tolerance = USL - LSL

    mean = data.mean()

    DNS = min(mean - LSL, USL - mean)

    stdev = data.std()

    ppk = DNS/(3*stdev)

    return {
        "Ppk": ppk,
    }