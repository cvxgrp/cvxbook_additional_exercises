% data for generator dispatch problem
% demand data
D = 2; % number of days
T = D*24*4; % number of 15 minute intervals
t= (1:T)/4; % time, in hours
rand('state',0);
d = 8+ ... % constant demand 
    4*sin(2*pi*t/24) +...  % diurnal variation 
    0.05*t+...  % a linear trend component 
    1.5*rand(1,T); % random demand variation
% generator data
n = 4; % number of generators
Pmax = [6 5 4 2];  % generator capacities
Pmin = [3 1 1 0];  % generator capacities
R = [0.1 0.2 0.5 1.5];  % ramp-rate limits
alpha = [1 1.2 1.5 2]; % linear cost fct coeffs
beta = 0.1*ones(1,n); % quadratic cost fct coeffs
gamma = [3 0.5 0.5 0.1]; % power change cost fct coeffs


% plotting code; replace p and Q below with correct values
p = ones(n,T);  % generator powers
Q = ones(1,T);  % prices
subplot(3,1,1)
plot(t,d);
title('demand')
subplot(3,1,2)
plot(t,p);
title('generator powers')
subplot(3,1,3)
plot(t,Q);
title('power prices')
