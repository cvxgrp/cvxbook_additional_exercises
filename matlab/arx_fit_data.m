clear; close all; 
% Parameters
M = 10;
T=200;
N = 3*T;
p = 0.2;
rng('default');
rng(2016);

beta_true = 2*rand(M,1)-1;
beta_true = beta_true/norm(beta_true,1);
x_true  = (rand(N, 1) < p).*randn(N, 1);
y_long = filter(1,[1; -beta_true],x_true );

% Only observe a length T subsequence.
y = y_long(1+T:T+T);
