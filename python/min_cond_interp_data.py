import numpy as np
np.random.seed(0)

# n is the dimension of each point, N is the number of points
# X is a matrix of size n x N, where each column corresponds to one 
# of the points
n, N = 5, 6
X = np.random.randn(n, N)
X = X / np.linalg.norm(X, axis=0)
P_feas = np.random.randn(n, n)
P_feas = P_feas @ P_feas.T
y = np.diag(X.T @ P_feas @ X)



