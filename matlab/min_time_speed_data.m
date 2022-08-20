% Minimum time speed profile along a road.

N = 50; % number of intervals
m = 1500; % mass of vehicle
d = 200; % distance between knot points
h = (100*sin((1:N+1)/(N+1)*5*pi/2+pi/4) + ...
    [zeros(1,10) -10*(1:10) +6*(1:31)-100])'; % elevation at knot points
eta = .26*35*10^6; % engine efficiency and energy content of the fuel

rho = 1.2; % density of air, used in calculation of C_D
A = 2.4; % effective frontal area used in calculation of C_D
c_d = .5; %effective aerodynamic drag coefficient NOT C_D from the problem
C_D = .5*rho*A*c_d; % coefficient of drag 
clear rho A c_d;

P = 1500; % power of the onboard systems
F = 2; % total initial fuel
g = 9.8; % acceleration due to gravity

%random data for initial plotting, 
%you should replace these with the values you find
s = rand(N+1,1); % minimum time speed
sc = .2*ones(N+1,1); % constant fuel speed
f = rand(N+1,1); % minimum time fuel burn
fc = .2*ones(N+1,1); % constant fuel fuel burn.

figure
subplot(3,1,1)
plot((0:N)*d,h);
ylabel('height');
subplot(3,1,2)
stairs((0:N)*d,s,'b');
hold on
stairs((0:N)*d,sc,'--r');
legend('minimum time','constant burn')
ylabel('speed')
subplot(3,1,3)
plot((0:N)*d, f,'b');
hold on
plot((0:N)*d, fc,'--r')
xlabel('distance')
ylabel('fuel used')
