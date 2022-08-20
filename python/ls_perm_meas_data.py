import numpy as np

np.random.seed(0)
m=100
k=40 # max # permuted measurements
n=20
A=10*np.random.randn(m,n)
x_true=np.random.randn(n,1) # true x value
y_true = A.dot(x_true) + np.random.randn(m,1)
# build permuted indices
perm_idxs=np.random.permutation(m)
perm_idxs=np.sort(perm_idxs[:k])
temp_perm=np.random.permutation(k)
new_pos=np.zeros(k)
for i in range(k):
  new_pos[i] = perm_idxs[temp_perm[i]]
new_pos = new_pos.astype(int)
# true permutation matrix
P=np.identity(m)
P[perm_idxs,:]=P[new_pos,:]
true_perm=[]
for i in range(k):
  if perm_idxs[i] != new_pos[i]:
    true_perm = np.append(true_perm, perm_idxs[i])
y=P.dot(y_true)
new_pos = None
