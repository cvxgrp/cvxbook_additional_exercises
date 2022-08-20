# basic data for multi-period liability clearing problem

import numpy as np

n = 7
L1 = np.array(
    [[0., 90, 0, 3, 79, 0, 0],
     [57, 0, 69, 37, 0, 94, 56],
     [79, 53, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 73, 20],
     [0, 0, 42, 0, 0, 0, 90],
     [0, 34, 0, 0, 13, 0, 0],
     [38, 0, 0, 94, 85, 22, 0]]
)
c1 = np.array([10., 146., 30., 10., 10., 10., 83.])

np.testing.assert_array_less(L1 @ np.ones(n) - L1.T @ np.ones(n), c1)
