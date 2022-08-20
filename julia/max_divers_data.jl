using LinearAlgebra, Random

Random.seed!(364)

n = 20

# _A and _C are internal - you don't need them.
_A = randn(2*n,n)
_C = diagm(0.5*exp.(randn(n)))

Sigma = _C*_A'*_A*_C
Sigma = 0.5*(Sigma + Sigma')
M = ones(n)*0.2
sigma = sqrt.(diag(Sigma))

# PLEASE USE THE FOLLOWING CODE TO PLOT YOUR SOLUTION
# Replace x_max_divers and x_min_variance with your optimal values
# using Plots
# idx = 1:40
# bar(idx[isodd.(idx)]./2, x_max_divers, bar_width=0.5, label="Max diversification")
# bar!(idx[iseven.(idx)]./2, x_min_variance, bar_width=0.5, label="Min variance")