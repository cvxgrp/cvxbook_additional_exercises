using Random
using Distributions
Random.seed!(1)

n = 10
F = randn((10, 10))
Sigma = F' * F
T = 10
a = [0.2 0.1 0.2 0.4 0.8 1.0 1.0 0.8 0.7 0.8]
x = zeros((n, T))
y = zeros((n, T))
for t in 1:T
    dist = MvNormal(zeros(n), a[t]*Sigma)
    x[:, t] = rand(dist)
    y[:, t] = rand(dist)
end
