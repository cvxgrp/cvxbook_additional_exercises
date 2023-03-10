import numpy as np

m = 4 # the number of raw materials
n = 2 # the number of blended materials
q = 3 # the number of constituents

# the ith column of C is c_i
C = np.array([[ .9,  .8, .7, .6],
              [.08, .12, .2, .2],
              [.02, .08, .1, .2]])

# bounds on the blended product concentration
c_min = np.array([[.85, 0.65],
                    [  0,  0],
                    [  0,  0]])
c_max = np.array([[ 1,  1 ],
                  [.1, .18],
                  [.05, .17]])

FTilde = np.array([10, 10]) # limit on the flow rate of the blended material
F = np.array([7, 2, 6, 3]) # availibility of raw materials

p = np.array([15, 13, 11, 8]) # price of raw materials
pTilde = np.array([21, 18]) # price of the blended material


