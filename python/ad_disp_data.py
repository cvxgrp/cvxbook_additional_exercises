import cvxpy as cvx
import numpy as np

np.random.seed(0)
n = 100   #number of ads
m = 30    #number of contracts
T = 60    #number of periods

#number of impressions in each period
I = 10*np.random.rand(T, 1); I = np.asmatrix(I)
#revenue rate for each period and ad
R = np.random.rand(n, T); R = np.asmatrix(R)
#contract target number of impressions
q = T/float(n)*50*np.random.rand(m, 1); q = np.asmatrix(q)
#penalty rate for shortfall
p = np.random.rand(m, 1); p = np.asmatrix(p)
#one column per contract. 1's at the periods to be displayed
Tcontr = np.matrix(np.random.rand(T, m)>.8, dtype = float)
Acontr = np.zeros((n, m)); Acont = np.asmatrix(Acontr)
for i in range(n):
    contract=int(np.floor(m*np.random.rand(1)))
    #one column per contract. 1's at the ads to be displayed
    Acontr[i,contract]=1
