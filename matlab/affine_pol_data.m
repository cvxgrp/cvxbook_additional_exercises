% affine policy.
m = 20; n = 10; p = 5;

randn('state',0); rand('state',0);
A = randn(m,n);
c = rand(n,1);
b0 = ones(m,1);
B = .15*sprandn(m,p,.3);
