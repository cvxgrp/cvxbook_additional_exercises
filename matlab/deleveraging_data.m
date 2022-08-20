% data file for de-leveraging problem
clear all;
rand('state', 1);
randn('state', 1);
gamma = 6;
T = 15;
n = 10;
mu = 20*randn(n, 1);
S = randn(n, n);
Sigma = S'*S+eye(n)*0.15;
Linit = 9.5;
Lnew = 5;
kappa  = rand(n, 1)*10;
lambda = rand(n, 1)*20;
