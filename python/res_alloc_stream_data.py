# resource allocation for stream processing.
import numpy as np
import scipy.io as sio

def get_value(mat, name):
    value = mat[name]
    return value[0][0] if np.shape(value) == (1, 1) else value

mat = sio.loadmat("res_alloc_stream_data.mat")

J = get_value(mat, "J")  # number of job types
P = get_value(mat, "P")  # number of process types
n = get_value(mat, "n")  # number of system resources

R = get_value(mat, "R").astype(float)  # job process matrix
x_tot = get_value(mat, "x_tot")  # total resources available
A = get_value(mat, "A")
x_min = get_value(mat, "x_min")  # minimum resources to run each process
w = get_value(mat, "w")
t_tar = get_value(mat, "t_tar")  # target job traffic
l_max = get_value(mat, "l_max")  # maximum allowed job latency
