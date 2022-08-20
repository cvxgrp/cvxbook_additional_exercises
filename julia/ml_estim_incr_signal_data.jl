# A6.6, A6.7, and A14.8

# create problem data
srand(0);
N = 100;
# create an increasing input signal
xtrue = zeros(N);
xtrue[1:40] = 0.1;
xtrue[50] = 2;
xtrue[70:80] = 0.15;
xtrue[80] = 1;
xtrue = cumsum(xtrue);

# pass the increasing input through a moving-average filter
# and add Gaussian noise
h = [1, -0.85, 0.7, -0.3];
k = length(h);
yhat = conv(h, xtrue);
y = yhat[1:end-3] + randn(N);
