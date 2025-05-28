import cvxpy
from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt

figpath = "figures/"
# datapath = "/home/anqi/Documents/teaching/364a/final/data/time_reg_data/"

figpath = ""
datapath = ""

np.random.seed(3)

# Problem data.
n = 5
m = 500
# T = 25
T = 20
M = 200
lams = np.logspace(-2, 2, 50)
# p = 0.15

# Generate training/test sets.
theta_true = np.random.randn(n,T)
X_train = np.random.randn(m,n)
t_train = np.random.choice(np.arange(1,T+1), m)
t_train = t_train - 1   # Python zero-indexing.

y_train = np.zeros(m)
# for i in range(m):
#	if np.random.uniform() <= p:
#		t = np.random.choice(np.arange(T))
#	else:
#		t = t_train[i]
#	y_train[i] = X_train[i].dot(theta_true[:,t])
# y_train = y_train + np.random.randn(m)
y_train = np.vstack([X_train[i]*theta_true[:,t_train[i]] for i in range(m)])
y_train = y_train[:,0] + np.random.randn(m)

# np.savetxt(datapath + "X_train.csv", X_train, delimiter = ",")
# np.savetxt(datapath + "t_train.csv", t_train + 1, delimiter = ",")
# np.savetxt(datapath + "y_train.csv", y_train, delimiter = ",")

X_test = np.random.randn(M,n)
t_test = np.random.choice(np.arange(1,T+1), M)
t_test = t_test - 1
# y_test = np.zeros(M)
# for i in range(M):
#	if np.random.uniform() < p:
#		t = np.random.choice(np.arange(T))
#	else:
#		t = t_test[i]
#	y_test[i] = X_test[i].dot(theta_true[:,t])
# y_test = y_test + np.random.randn(M)
y_test = np.vstack([X_test[i]*theta_true[:,t_test[i]] for i in range(M)])
y_test = y_test[:,0] + np.random.randn(M)

# np.savetxt(datapath + "X_test.csv", X_test, delimiter = ",")
# np.savetxt(datapath + "t_test.csv", t_test + 1, delimiter = ",")
# np.savetxt(datapath + "y_test.csv", y_test, delimiter = ",")

# Define problem.
theta = Variable((n,T))
lam_parm = Parameter(pos = True)

y_hat_train = vstack([X_train[i]*theta[:,t_train[i]] for i in range(m)])
y_hat_train = y_hat_train[:,0]

err_train = sum_squares(y_hat_train - y_train)
reg = sum(norm2(diff(theta), axis=1))
obj = err_train + lam_parm*reg
prob = Problem(Minimize(obj))

# Solve problem and save test error.
y_hat_test = vstack([X_test[i]*theta[:,t_test[i]] for i in range(M)])
y_hat_test = y_hat_test[:,0]

err_test = sum_squares(y_hat_test - y_test)
err_test_vec = np.zeros(50)
for k in range(50):
	lam_parm.value = lams[k]
	prob.solve()
	err_test_vec[k] = err_test.value

# Plot test error versus lambda.
plt.plot(lams, err_test_vec)
# plt.title("Test Error vs. Regularization Parameter")
plt.xscale("log")
plt.xlabel("$\lambda$")
plt.savefig(figpath + "time_reg_err.pdf", bbox_inches = "tight")
plt.show()

idx = np.argmin(err_test_vec)
lam_best = lams[idx]
print("Minimum test error:", err_test_vec[idx])
print("Best value of lambda:", lam_best)

# Plot theta for several values of lambda.
# Best lambda.
lam_parm.value = lam_best
prob.solve()
theta_best = theta.value

t_rep = np.array(n*[np.arange(1,T+1)])
plt.plot(t_rep.T, theta_best.T)
plt.title("Optimal Value of $\\theta$ for $\lambda = \lambda^{\star}$")
plt.xlabel("$t$")
plt.ylim(-2.0, 2.0)
plt.savefig(figpath + "time_reg_theta_best.pdf", bbox_inches = "tight")
plt.show()

# Best lambda scaled up by a factor of 10.
lam_parm.value = 5*lam_best
prob.solve()
theta_hi = theta.value

plt.plot(t_rep.T, theta_hi.T)
plt.title("Optimal Value of $\\theta$ for $\lambda = 5\lambda^{\star}$")
plt.xlabel("$t$")
plt.ylim(-2.0, 2.0)
plt.savefig(figpath + "time_reg_theta_hi.pdf", bbox_inches = "tight")
plt.show()

# Best lambda scaled down by a factor of 10.
lam_parm.value = lam_best/5
prob.solve()
theta_lo = theta.value

plt.plot(t_rep.T, theta_lo.T)
plt.title("Optimal Value of $\\theta$ for $\lambda = \lambda^{\star}/5$")
plt.xlabel("$t$")
plt.ylim(-2.0, 2.0)
plt.savefig(figpath + "time_reg_theta_lo.pdf", bbox_inches = "tight")
plt.show()
