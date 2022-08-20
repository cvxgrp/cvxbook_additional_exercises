using Random

# simple_portfolio_data
n = 20;
Random.seed!(7);
pbar = ones(n)*0.03 + [rand(n-1); 0]*0.12;
Random.seed!(7);
S = randn(n,n);
S = S'*S;
S = S/maximum(abs.(diag(S))) * 0.2;
S[:,n] = zeros(n);
S[n,:] = zeros(n)';
x_unif = ones(n)/n;
