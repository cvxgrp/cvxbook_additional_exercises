import numpy as np
P = np.loadtxt("asset_prices.csv", delimiter=",", skiprows=1); # prices
T, n = np.shape(P);
B = 1000;
