randn('state',0); rand('state',0);

n = 10; m = 15;

A = rand(m,n); xint = rand(n,1);
b = A*xint+2*rand(m,1);
c = rand(n,1);
