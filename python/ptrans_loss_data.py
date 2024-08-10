import numpy as np
import matplotlib.pyplot as plt

# Data for power flow problem
n = 11  # total number of nodes
m = 19  # number of edges (transmission lines)
k = 3   # number of generators

np.random.seed(1)
Gmax = np.array([3, 5, 9])         # maximum generator power
a = np.array([10, 8, 3])           # generator linear costs
b = np.array([0.2, 0.3, 0.1])      # generator quadratic costs
l = 1 + np.random.rand(n - k)      # network loads
R = np.ones(m)                     # initial assignment of conductor radii
Rmax = 1.5 * np.ones(m)            # maximum conductor radii
Rmin = 0.5 * np.ones(m)            # minimum conductor radii
alpha = 0.05                       # conductor loss coefficient
sigma = 4.5                        # coeff for max line power

# Graph incidence matrix
A = np.array([
    [-1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0, -1,  0,  0, -1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1],
    [ 0,  0,  0,  0,  1, -1,  0,  1, -1,  0,  1,  1,  0,  0,  0,  0,  1,  0,  0],
    [ 1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  1,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  1,  0,  0,  0, -1,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0, -1,  0,  0,  0,  1,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  1, -1,  0,  0,  0, -1,  0],
    [ 0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  1,  1,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, -1,  1,  0]
])

# Node x-y coordinates
XY = np.array([
    [1.2, 4.8],  # node 1
    [0.8, 3.4],  # node 2
    [6.7, 2.7],  # node 3
    [3.8, 4.1],  # node 4
    [3.2, 4.8],  # node 5
    [5.9, 4.8],  # node 6
    [1.8, 4.1],  # node 7
    [5.9, 3.7],  # node 8
    [3.5, 2.7],  # node 9
    [5.4, 2.8],  # node 10
    [2.8, 3.5]   # node 11
])

# Node distances
L = np.zeros(m)
idx = np.zeros((m, 2), dtype=int)
for j in range(m):
    idx[j, 0] = np.where(A[:, j] == 1)[0][0]
    idx[j, 1] = np.where(A[:, j] == -1)[0][0]
    L[j] = np.linalg.norm(XY[idx[j, 0], :] - XY[idx[j, 1], :])

Vmax = np.dot(L, R ** 2)  # Volume constraint

# Node adjacency matrix
Ad = -A @ A.T
np.fill_diagonal(Ad, 0)

epsx, epsy = 0.05, 0.15  # text placing offset 

# Plotting the network graph
plt.figure()

# Connect edges
for i in range(len(Ad)):
    for j in range(i, len(Ad)):
        if Ad[i, j] != 0:
            plt.plot([XY[i, 0], XY[j, 0]], [XY[i, 1], XY[j, 1]], '-k')

# Label generator nodes
for j in range(k):
    plt.plot(XY[j, 0], XY[j, 1], 'rs', markerfacecolor='r', markersize=12)
    plt.text(XY[j, 0] - epsx, XY[j, 1] + epsy, str(j + 1), fontsize=10)

# Label load nodes
for j in range(k, n):
    plt.plot(XY[j, 0], XY[j, 1], 'ob', markersize=15)
    plt.text(XY[j, 0] - epsx, XY[j, 1] + epsy, str(j + 1), fontsize=10)

# Plot directions and edges
for i in range(m):
    x = XY[idx[i, 0], 0] - 1 / 6 * (XY[idx[i, 0], 0] - XY[idx[i, 1], 0])
    y = XY[idx[i, 0], 1] - 1 / 6 * (XY[idx[i, 0], 1] - XY[idx[i, 1], 1])
    plt.plot(x, y, 'rs', markerfacecolor='g', markersize=5)
    xtxt = XY[idx[i, 0], 0] - 1 / 2 * (XY[idx[i, 0], 0] - XY[idx[i, 1], 0])
    ytxt = XY[idx[i, 0], 1] - 1 / 2 * (XY[idx[i, 0], 1] - XY[idx[i, 1], 1])
    plt.text(xtxt - epsx, ytxt + epsy, str(i + 1), fontsize=10, backgroundcolor='g')

plt.axis('off')
plt.show()
