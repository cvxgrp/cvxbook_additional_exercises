# Parameters
M = 10;
T=200;
N = 3*T;
p = 0.2;
srand(2017);

# Data generation: 
beta_true = 2*rand(M)-1;
beta_true = beta_true/norm(beta_true,1);
x_true = (rand(N) .< p).*randn(N);

y_shifted = zeros(N+M+1);
# Shift y by M, then generate y using AR model
for t =1:N
    y_shifted[t+M+1] = x_true[t]+ sum( flipdim(beta_true,1).*y_shifted[t+M+1-M:t+M])
end
# Only observe a length T subsequence.
y= y_shifted[1+T+M:T+T+M]