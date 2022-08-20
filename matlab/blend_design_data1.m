% data file for circuit blending problem
rand('state',0);

n = 10; % number of variables
k = 8;  % number of designs

% first make some posynomials for power, delay, and area
%
p_exp_1 = 0.5+rand(n,1);
p_exp_2 = rand(n,1);
d_exp_1 = -0.5-rand(n,1);
d_exp_2 = -rand(n,1);

% now generate widths
% W_max gives minimum width for each design
% W_min gives maximum width for each design
W_min = ones(n,1)*[1,  1,  1,  2,  3,  6,  7,  8];
W_max = ones(n,1)*[2,  4, 10,  8,  7,  9, 10,  9];
% Two methods for generating bounded widths:
% First method: generate uniform distribution between W_min and W_max
W = W_min + (W_max-W_min).*rand(n,k)
% Second method: generate uniform distribution between 1 and 10,
%  then truncate to W_min and W_max
%%W = 1 + 9*rand(n,k);
%%W = min(max(W, W_min), W_max)

lengths = ones(n,1)+rand(n,1);  % device lengths


P = zeros(1,k);
D = zeros(1,k);
A = zeros(1,k);
for i=1:k
w=W(:,i);
P(i)= sum(w.^p_exp_1)+ sum(w.^p_exp_2);
D(i)= sum(w.^d_exp_1)+ sum(w.^d_exp_2);
A(i)= lengths'*w;
end

% print out design objectives achieved (power; delay; area)
[P;D;A] 

%%Pspec = 100;
%%Dspec = 8;
%%Aspec = 88;
Pspec = 85;  % (will need Pspec=80 for linear interpolation to not work, if using second method of generating W)
Dspec = 8.5;
Aspec = 75;
cvx_begin
variable theta(k)
sum(theta) == 1;
theta >= 0;
minimize (log(P)*theta);
log(D)*theta <= log(Dspec);
log(A)*theta <= log(Aspec);
cvx_end
% check design power (make sure less than Pspec)
Pdes = exp(log(P)*theta)


% test linear interpolation
% if this is infeasible, then linear interpolation will not work
cvx_begin
variable theta_lin(k)
sum(theta_lin) == 1;
theta_lin >= 0;
%minimize(P*theta_lin)
P*theta_lin <= Pspec;
D*theta_lin <= Dspec;
A*theta_lin <= Aspec;
cvx_end
%P*theta_lin


