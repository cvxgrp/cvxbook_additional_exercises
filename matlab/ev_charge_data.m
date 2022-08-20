N = 7;  % number of vehicles
T = 100; % number of time periods

Qdes = zeros(N,T);
Qdes(1,T/2) = 0.8;
Qdes(2,T/4) = 0.7;
Qdes(3,3*T/4) = 0.8;
Qdes(4,T/5) = 0.8;
Qdes(5,T/4) = 0.5;  Qdes(5,3*T/4) = 0.4;
Qdes(6,T/2) = 1;
Qdes(7,T/4) = 0.5;
Qdes = cumsum(Qdes,2);
Qdes(:,T) = 1;

Cmax = 4/T;
Pmax = N/4*Cmax;