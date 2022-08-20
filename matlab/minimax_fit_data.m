%% data for minimax linear fitting
% provides A, x_true, y

rand('seed',0);
randn('seed',0);

m = 100;
n = 50;

A = randn(m,n);
x_true = 10*randn(n,1);
v = randn(m,1);
y = A*x_true + v;

clear v;
