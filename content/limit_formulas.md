## Calculating XmR Chart Process Limits

The defining features of the XmR chart are the three process limits: the Upper Process Limit (UPL), the Lower Process Limit (LPL), and the Upper Range Limit (URL). The UPL and LPL define how large or small a values must be before it represents a departure from the historic mean. The URL defines how large a moving range must be before it represents a departure from the average moving range. 

The UPL and LPL are calculated using the formulas:

[FIGURE_1]

Here, $\overline{\mathrm{X}}$ is the mean of the individual values, 2.660 (otherwise represented as $\mathrm{E}_2$) is a scaling factor, and $\overline{\mathrm{mR}}$ is the average moving range of the moving ranges. The 2.660 scaling factor is required to convert the average moving range into the appropriate amount of spread for the individual values. Although its value will change with respect to the size of the rational subgroup, for rational subgroups of size n = 1, the value of $\mathrm{E}_2$ will always be 2.660.

The URL is calculated using the formula:

[FIGURE_2]

Here, 3.268 (otherwise represented as $\mathrm{D}_4$) is a scaling factor and $\overline{\mathrm{mR}}$ is the average moving range of the moving ranges. The 3.268 scaling factor is required to convert the average moving range into the appropriate upper bound for the moving ranges.

[BUTTON_1]