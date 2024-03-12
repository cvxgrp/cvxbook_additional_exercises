import numpy as np

n = 3
m = 1
k = 3
omega = 2
kappa_max = 10

# A[0] is the matrix A_1,
# A[1] is the matrix A_2, and 
# A[2] is the matrix A_3
A = np.array([
    [[0.0, 4/3, 0.0],
     [-2, 0.0, -2],
     [0.0, 1, -3]],       # end of A_1
    [[0.0, 4/5, 0.0],
     [-2, 0.0, -2],
     [0.0, 2/3, -10/3]],  # end of A_2
    [[0.0, 8/3, 0.0],
     [-2, 0.0, -2],
     [0.0, 2, -12]]       # end of A_3
])
B = np.array([[0.0], [1/2], [0]])
