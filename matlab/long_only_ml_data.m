% Dimension of input
n = 20;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DATA GENERATION PROCESS
% NOT NEEDED TO SOLVE PROBLEM
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Set random variable seed
rng(0)

% Generate distribution with true mean mu
% and true covariance Sigma such that Sigma^(-1)mu >= 0
Sigma = rand(n, n);
Sigma = 0.5*(Sigma + Sigma');
Sigma = Sigma + n*eye(n);
temp_mu = rand(n,1);
res = Sigma \ temp_mu;
res = max(res, 0);
mu = Sigma*res;

% Draw N random samples from distribution
N = 25;
X = randn(n, N);
MU = zeros(n, N);
for i = 1:N
    MU(:,i) = mu;
end
Sq = sqrtm(Sigma);
X = Sq*X;
X = X + MU;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END OF DATA GENERATION PROCESS
%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GIVEN
% n: dimension of vecotr
% N: number of samples from distribution
% X: matrix containing  N samples from distribution (n x N)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%
% YOUR CODE BELOW
%%%%%%%%%%%%%%%%%%%%%%%%%%
