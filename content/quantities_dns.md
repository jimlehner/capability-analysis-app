### Distance to Nearer Specification
The distance to the nearest specification limit (DNS) is the distance between a dataset’s  mean and the nearest specification limit. It measures how well the process mean is centered relative to the specification limits. When the process mean is centered at the target, the distance from the mean to the LSL and the distance from the mean to the USL will converge.
To calculate the DNS, subtract the LSL from the mean and subtract the mean from the USL. The DNS will be the minimum of these two values. In practice, this is achieved using a MIN() function. After providing two arguments, a MIN() function returns the smaller of the two.

[FIGURE_DNS]