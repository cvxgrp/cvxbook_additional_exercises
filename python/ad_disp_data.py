import cvxpy as cvx
import numpy as np

np.random.seed(0)
n = 100   #number of ads
m = 30    #number of contracts
T = 60    #number of periods

#number of impressions in each period
I = 10*np.random.rand(T)
#revenue rate for each period and ad
R = np.random.rand(n, T)
#contract target number of impressions
q = T/float(n)*50*np.random.rand(m)
#penalty rate for shortfall
p = np.random.rand(m)
#one column per contract. 1's at the periods to be displayed
Tcontr = np.matrix(np.random.rand(T, m)>.8, dtype = float)
Acontr = np.zeros((n, m))
Acont = Acontr
for i in range(n):
    contract=int(np.floor(m*np.random.rand(1)))
    #one column per contract. 1's at the ads to be displayed
    Acontr[i,contract]=1
