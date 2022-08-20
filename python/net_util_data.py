# From net_util_data.m ofEE364a final 2008.
# Data for network utility optimization.

import numpy as np
import scipy.io as sio

def get_value(mat, name):
    value = mat[name]
    return value[0][0] if np.shape(value) == (1, 1) else value

mat = sio.loadmat("net_util_data.mat")

n = get_value(mat, "n")
m = get_value(mat, "m")
R = get_value(mat, "R")
c = get_value(mat, "c")


