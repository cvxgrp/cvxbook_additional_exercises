%% simple_portfolio_data
rand('state', 5);
randn('state', 5);
n=20;
pbar = ones(n,1)*.03+[rand(n-1,1); 0]*.12;
S = randn(n,n);
S = S'*S;
S = S/max(abs(diag(S)))*.2;
S(:,n) = zeros(n,1);
S(n,:) = zeros(n,1)';
x_unif = ones(n,1)/n;
