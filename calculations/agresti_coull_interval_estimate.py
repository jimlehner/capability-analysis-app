import numpy as np

def binomial_point_estimate(data, USL, LSL, round_value=2):
    Y = ((data < LSL) | (data > USL)).sum()
    n = data.count()

    p_hat = round(Y/n, round_value)

    return {
        "Y" : Y,
        "n" : n,
        "p_hat": p_hat,
    }

def biased_point_estimate(data, USL, LSL, round_value=2):
    Y = ((data < LSL) | (data > USL)).sum()
    n = data.count()
    
    p_tilde = (Y + 2) / (n + 4)

    return {
        "Y" : Y,
        "n" : n,
        "p_tilde": p_tilde,
    }

def agresti_coull_interval_estimate(data, USL, LSL, round_value=2):
    Y = ((data < LSL) | (data > USL)).sum()
    n = data.count()

    p_hat = round(Y/n, round_value)
    
    p_tilde = round((Y + 2) / (n + 4), round_value)

    AG_upper = p_tilde + 1.96 * np.sqrt((p_tilde * (1 - p_tilde))/(n + 4))
    AG_lower = p_tilde - 1.96 * np.sqrt((p_tilde * (1 - p_tilde))/(n + 4))

    return {
        "Y": Y,
        "n": n,
        "p_hat": p_hat,
        "p_tilde": p_tilde,
        "AG_upper": AG_upper,
        "AG_lower": AG_lower
    }
