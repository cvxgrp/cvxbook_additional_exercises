% data for portfolio optimization with qualitative return forecasts
% provides n, l, u, Sigma, sig

rand('state', 0); 
randn('state', 0); 

n = 10; % number of stocks

c = 0.05 + randn(n,1)*0.1;
r = rand(n,1)*0.2;
l = c - r;
u = c + r;

Sigma = randn(n);   % capital Sigma
Sigma = 3*eye(n) + Sigma'*Sigma;
Sigma = Sigma/max(diag(Sigma));
Sigma = 0.2^2*Sigma;

sigma_max = sqrt(0.07);   % small sigma
