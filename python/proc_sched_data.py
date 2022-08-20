# Data for minimum energy processor speed scheduling.
import numpy as np
import matplotlib.pyplot as plt
n = 12  # number of jobs.
T = 16  # number of time periods.

Smin = 1.0  # min processor speed.
Smax = 4.0  # max processor speed.
R = 1.0     # max slew rate.

# Parameters in power/speed model.
alpha = 1.0
beta = 1.0
gamma = 1.0

# Job arrival times and deadlines.
A = np.matrix('0; 2;  3; 5; 8;  8; 10; 11; 12; 12; 13; 14')
D = np.matrix('2; 5; 10; 6; 8; 11; 12; 14; 14; 15; 13; 15')

# Total work for each job.
W = np.matrix('2; 4; 10; 2; 3; 2; 3; 2; 3; 4; 1; 4')

# Plot showing job availability times & deadlines.
plt.plot(A,list(range(n)),'k*')
plt.plot(D+1,list(range(n)),'ko')
for i in range(n):
    plt.plot(np.array([A[i,0],D[i,0]+1]),np.array([i,i]),'k-')
plt.xlabel('time t'); plt.ylabel('job i')
plt.show()



# s = Tx1 vector of speeds and theta = Txn matrix of allocations
#r = lambda: np.random.randint(0,255)
#for i in range(n):
#    rand_color = ('#%02X%02X%02X' % (r(),r(),r()))
#    plt.bar(range(T),np.multiply(theta[:,i],s),color = rand_color)
#plt.xlabel('time t'); plt.ylabel('speed st')
#plt.show()
