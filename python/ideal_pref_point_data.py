from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt

# Problem data
K = 8
n = 2

# List of candidate choices
c = [[0.314, 0.509], [0.185, 0.282], [0.670, 0.722], [0.116, 0.253],
     [0.781, 0.382], [0.519, 0.952], [0.953, 0.729], [0.406, 0.110]]
c = [np.array(x) for x in c]

# List of decisions. [i, j] means c[i] preferred over c[j]
d = [[0, 1], [2, 0], [2, 1], [0, 3], [1, 3], [2, 3], [4, 0],
     [4, 1], [2, 4], [4, 3], [0, 5], [5, 1], [2, 5], [5, 3],
     [4, 5], [6, 0], [6, 1], [2, 6], [6, 3], [4, 6], [6, 5],
     [0, 7], [7, 1], [2, 7], [7, 3], [4, 7], [5, 7], [6, 7]]

box = [[0] * 2 for a in range(n)]

# Put your code for finding the bounding box here.
# box[i][0] and box[i][1] should be the lower and upper bounds
# of the i-th coordinate respectively.

# Drawing the bounding box
plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.scatter([c[i][0] for i in range(K)], [c[i][1] for i in range(K)])
plt.plot([box[0][0], box[0][1], box[0][1], box[0][0], box[0][0]],
         [box[1][0], box[1][0], box[1][1], box[1][1], box[1][0]])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
print(('Width of bounding box = ' + str(box[0][1] - box[0][0])))
print(('Height of bounding box = ' + str(box[1][1] - box[1][0])))

