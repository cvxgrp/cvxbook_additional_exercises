# create problem data
using Random
Random.seed!(0);
N = 100;
# create an increasing input signal
xtrue = zeros(N);
xtrue[1:40] .= 0.1;
xtrue[50] = 2;
xtrue[70:80] .= 0.15;
xtrue[80] = 1;
xtrue = cumsum(xtrue);

function _conv(x, y)
    n = length(x)
    m = length(y)
    z = zeros(n+m-1)
    for i in 1:n
        for j in 1:m
            z[i+j-1] += x[i]*y[j]
        end
    end
    return z
end

# pass the increasing input through a moving-average filter
# and add Gaussian noise
h = [1, -0.85, 0.7, -0.3];
k = length(h);
yhat = _conv(h, xtrue);
y = yhat[1:end-3] + randn(N);