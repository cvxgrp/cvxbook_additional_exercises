% data file for worst-case variance problem
clear all;
rand('state', 2);
randn('state', 2);
n = 10;
[Q, R] = qr(rand(n));
Sigma = Q'*diag(rand(n, 1))*Q;
mu = randn(n, 1);

R = 5;
R_wc = 10;

clear Q
