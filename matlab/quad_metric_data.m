%% data for learning a quadratic metric
% provides X, Y, d, X_test, Y_test, d_test

rand('seed',0);
randn('seed',0);

n = 5;   % dimension
N = 100;  % number of distance samples
N_test = 10;

X = randn(n,N);
Y = randn(n,N);
X_test = randn(n,N_test);
Y_test = randn(n,N_test);

P =randn(n,n);
P = P*P'+eye(n);
sqrtP = sqrtm(P);

d = norms(sqrtP*(X-Y)); % exact distances
d = pos(d+randn(1,N)); % add noise and make nonnegative
d_test = norms(sqrtP*(X_test-Y_test)); 
d_test = pos(d_test+randn(1,N_test));

clear P sqrtP;
