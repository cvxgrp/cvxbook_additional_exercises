import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

T = 96
t = np.linspace(1, T, num=T).reshape(T,1)
p = np.exp(-np.cos((t-15)*2*np.pi/T)+0.01*np.random.randn(T,1))
u = 2*np.exp(-0.6*np.cos((t+40)*np.pi/T) - 0.7*np.cos(t*4*np.pi/T)+0.01*np.random.randn(T,1))


plt.figure(1)
plt.plot(t/4, p); 
plt.plot(t/4, u, 'r'); 
plt.show()
