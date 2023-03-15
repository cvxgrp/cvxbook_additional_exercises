### THIS FILE GENERATES d, K, N, N_test, TRAINING DATA X_train, pi_train, TEST DATA X_test, pi_test AND 
### THE PROJECTION FUNCTION Pi()
### YOU DO NOT NEED TO READ THIS FILE TO DO THE PROBLEM


import numpy as np

def Pi(y):
    """Returns the rakning of the argument.

    :param y: a 2d array of size N x K or a 1d array of size K, N input vectors/1 vector to generate the rankings
    
    :return: a 2d numpy array with ith row being the ranking of the ith row of y if y is a 2d array, 
    and a 1d ranking (numpy array) if y is a 1d array
    """
    y = np.array(y)
    if y.ndim == 1:
        ranking = np.argsort(np.argsort(y)) + 1
    else:
        ranking = np.argsort(np.argsort(y, axis = -1), axis = -1) + 1
    return ranking

# Data generation
N = N_test = 500
d = 20
K = 10

np.random.seed(0)

# Generate the true theta matrix
theta_true = np.random.randn(K,d)
theta_true /= np.linalg.norm(theta_true[:])

# Sample x_i from standard Gaussian
X_test = np.hstack([np.random.randn(N_test,  d-1), np.ones((N_test, 1))])
X_train = np.hstack([np.random.randn(N,  d-1), np.ones((N, 1))])

# Generate the true features y = theta x and add noise to them
Y_train, Y_test = X_train.dot(theta_true.T), X_test.dot(theta_true.T)

# Add 15dB of noise to the observed y to generate noisy rankings
noise_snr = 15.
sigma_noise = 10 ** (-0.05 * noise_snr) / np.sqrt(K)
Y_train, Y_test = Y_train + sigma_noise * np.random.randn(N, K), Y_test + sigma_noise * np.random.randn(N_test, K)

# Get the rankins of the observed noisy data
pi_train, pi_test = Pi(Y_train), Pi(Y_test)