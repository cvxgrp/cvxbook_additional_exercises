import numpy as np

### Data ###
# This data file consists of parameters for the flight simulator problem. Some
# of the parameters are inspired by the paper "Grant, P., & Haycock, B. (2008).
# Effect of jerk and acceleration on the perception of motion strength. Journal
# of Aircraft, 45(4), 1190–1197." It contains the following parameters:
"""
- h: time step (s)
- P_max: position limit (m)
- position: T-array of reference position (m)
"""

h = 0.1
P_max = 0.6
position = np.array(
    [
        0.0,
        0.03302791,
        0.12840479,
        0.3084541,
        0.5859962,
        0.96290951,
        1.42991972,
        1.9676406,
        2.54874986,
        3.14105557,
        3.71110918,
        4.22795958,
        4.66662684,
        5.01090576,
        5.25518468,
        5.3994636,
        5.44374253,
        5.38802145,
        5.23230037,
        4.9765793,
        4.62085822,
        4.16513714,
        3.60941606,
        2.95369499,
        2.19797391,
        1.34225283,
        0.38512884,
        -0.67744937,
        -1.85172678,
        -3.14544116,
        -4.56695465,
        -6.12431524,
        -7.82435349,
        -9.67191597,
        -11.66932126,
        -13.81609974,
        -16.10904632,
        -18.54258016,
        -21.10937096,
        -23.80116177,
    ]
)
