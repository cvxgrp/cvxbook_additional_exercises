import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


"""
You should use the following variables and functions:
 - T, n, K: dimensions of the problem
 - Pi_train, Pi_test
 - plot_prediction_error(hat_Pi, Pi, optional filename)
    - hat_Pi should be a n x (T - K) matrix
        and  Pi should be a n x T matrix
"""

__all__ = [
    'T', 'n', 'K', 'Pi_train', 'Pi_test', 'plot_prediction_error'
]

np.random.seed(1001)
T = T_test = 100 # train and test set sizes
n = 4
K = 2

start = 50 # run MC for this many steps before recording the data
delta = 0.3 # noise std in the noisy K-Markov model
Pi = np.zeros((n, T + T_test + start))
mu = 0; sigma = 2

def K_Markov_step(t, Pi, A1_true, A2_true):
    res = A1_true @ Pi[:, t] + A2_true @ Pi[:, t-1]
    return res

# generate initial K distributions and pi_eq
for i in range(K):        
    x = np.random.normal(mu, sigma, n)
    Pi[:, i] = np.exp(x)/sum(np.exp(x))
    assert np.allclose(Pi[:, i].sum(), 1) and (Pi[:, i] >= 0).all()
# column sums of coefficient matrices A_i
theta = 1./np.arange(1, K+1)
theta /= theta.sum()
# transition matrices: A1_true \approx I; A2_true enforces different ratios
A1_true = np.eye(n) + 1e-5 * np.random.rand(n, n)
A1_true = (A1_true / A1_true.sum(axis=0).reshape(1, n)) * theta[0]
assert np.allclose(A1_true.sum(axis=0), theta[0])
A2_true = np.random.rand(n, n)
A2_true[1,:] *= 3; A2_true[2,:] *=2; A2_true[3,:] *= 4
A2_true = (A2_true / A2_true.sum(axis=0).reshape(1, n)) * theta[1]
assert np.allclose(A2_true.sum(axis=0), theta[1]) and np.allclose(1, A1_true.sum(axis=0)+A2_true.sum(axis=0))
# noisy K-Markov model to generate probability distributions \pi_{t+1}
T_total = T + T_test + start
for t in range(K-1, T_total-1):
    y_t = K_Markov_step(t, Pi, A1_true, A2_true)
    log_y_t = np.log(y_t + 1e-8) + np.random.normal(0, delta, n)
    Pi[:, t+1] = np.exp(log_y_t)/sum(np.exp(log_y_t))
    assert np.allclose(Pi[:, t+1].sum(), 1) and (Pi[:, t+1] >= 0).all()
Pi_train = Pi[:, start:T+start]
Pi_test =  Pi[:, T+start:]

def plot_prediction_error(hat_Pi, Pi, filename=''):
    Delta_Pi = np.abs(hat_Pi - Pi[:,K:])
    fig = plt.figure(figsize=(12, 5), dpi=100)
    plt.stackplot(np.arange(K, T), Delta_Pi,
                  labels=[f'$|\\hat\\pi_{i} - \\pi_{i}|$' for i in range(n)])
    plt.legend()
    if filename:
        fig.savefig(filename)
    plt.show()
