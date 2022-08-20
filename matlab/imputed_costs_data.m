rand('state',0);
m = 10; % number of inequalities
n = 5; % number of variables
r = 10; % number of samples
A = rand(m,n);
B = rand(m,r);
c_true = A'*rand(m,1);
c_true = c_true/c_true(1);

% cvx_quiet(true)
cvx_begin
variable X(n,r)
minimize(sum(c_true'*X))
A*X >= B;
cvx_end
