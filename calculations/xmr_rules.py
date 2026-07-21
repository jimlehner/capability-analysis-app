def apply_rule_2(data, mean):
    above = [v > mean for v in data]
    run_mask = [False] * len(data)

    # Check for runs of eight above and below central line
    for direction in [True, False]:
        count = 1
        for i in range(1, len(above)):
            if above[i] == direction and above[i-1] == direction:
                count += 1
            else:
                if above[i-1] == direction and count >= 8:
                    for j in range(i - count, i):
                        run_mask[j] = True
                count = 1
        
        # Final run
        if above[-1] == direction and count >= 8:
            for j in range(len(above) - count, len(above)):
                run_mask[j] = True

    return run_mask

def apply_rule_3(data, UPL, LPL, mean):
    PLR = UPL - LPL
    quartile = PLR / 4
    upper_zone = UPL - quartile
    lower_zone = LPL + quartile

    zone_mask = [False] * len(data)

    i = 0
    while i <= len(data) - 4:
        window = list(data[i:i+4])

        all_above = all(mean <= v <= UPL for v in window)
        all_below = all(LPL <= v <= mean for v in window)

        if all_above and sum(v >= upper_zone for v in window) >= 3:
            for j in range(i, i+4):
                zone_mask[j] = True
            # skip forward until we find a point not in the upper zone
            i += 4
            while i < len(data) and upper_zone <= data[i] <= UPL:
                i += 1

        elif all_below and sum(v <= lower_zone for v in window) >= 3:
            for j in range(i, i+4):
                zone_mask[j] = True
            # skip forward until we find a point not in the lower zone
            i += 4
            while i < len(data) and LPL <= data[i] <= lower_zone:
                i += 1

        else:
            i += 1

    return zone_mask