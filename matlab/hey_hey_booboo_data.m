% matlab data file
%
% Data for the problem of dodging Yogi bear so he doesn't steal your
% picnic basket.
% Chi-square thresholds for given confidence levels
threshold_05 = 5.991 / 200

% Time discretization size
delta = .2

% Drag force without motion
alpha = .1

% Action transfer rate
beta = .5

% Initial bear/human velocity is zero
v_init = randn(2,1)

% Initial bear position
x_init_bear = randn(2,1)

% Initial human position
x_init_human = [-5.0; 0]

% Goal position
x_safe = [5.0; 0]

% Maximum human force
u_max = .5

% The number of steps to take
k = 400

% Make V a k-by-2 matrix of rotating directions, but slightly wrong.
thetas = linspace(0, pi, k)
kappa = .85

V = [cos(kappa * thetas); sin(kappa * thetas)]