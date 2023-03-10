import numpy as np
import scipy.linalg as la
from numpy.random import RandomState
from scipy import signal

# Parameters
T = 400
k = 20
N = T+k
p=0.1
sigma = 0.0001
#  Random Model with fixed seed
rn = RandomState(364)

w_true = rn.rand(k)
index =np.argmax(np.abs(w_true))
w_true = np.roll(w_true,-index)
w_true = w_true/w_true[0]


x_true = rn.randn(T)
x_true = rn.binomial(1,p,np.shape(x_true))*x_true
y_true = np.real(np.fft.ifft( np.fft.fft(x_true,N)/np.fft.fft(w_true,N),N))
y= y_true[k:T+k]+ sigma* rn.randn(T)

def inverse_ker(w, len=N):
	w_inv = np.real(np.fft.ifft(1/np.fft.fft(w,len),len))
	return w_inv
