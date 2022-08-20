% generate data for energy portfolio problem
% returns quantities N, Nval, n, b, cmax, cmin, A, Aval, d, dval
rand('state',0);

N=1000;  % number of samples used to optimize portfolio
Nval=10000; % number of samples used to validate portfolio

n_wind=4; % number of wind farms

% plant costs including subsidies, etc.
b_coal=140; % coal plant cost
b_wind=60; % wind farm cost
b_solar=55; % solar farm cost

b=[b_coal;b_wind*ones(n_wind,1);b_solar];

n=length(b); % we'll have n_wind wind farms + 1 coal plant + 1 solar farm

% energy production capacity limits for each type of plant
cmax_coal=35;
cmax_wind=10;
cmax_solar=20;
% stack into one vector cmax
cmax=[cmax_coal;cmax_wind*ones(n_wind,1);cmax_solar];
cmin=zeros(n,1); % cmin is zero for all plants

p=1100; % price to produce energy by the peakers

% generate random coal plant availability
poff = 0; % coal plant down some of the time
punif = 0.1; % prob mass uniformly distributed on [0,1]
% otherwise, coal plant fully functional
f = 1/punif; g = -poff/punif;
acoal=f*rand(1,N+Nval)+g;
acoal = max(acoal,0);  % clip a to be >= 0
acoal = min(acoal,1); % clip a to be <= 1

% generate random wind availability
poff = 0.3; % no wind some of the time
punif = 0.6; % prob mass uniformly distributed on [0,1]
% otherwise, wind on full
f = 1/punif; g = -poff/punif;
awind=f*rand(n_wind,N+Nval)+g;
awind = max(awind,0);  % clip a to be >= 0
awind = min(awind,1); % clip a to be <= 1

% generate correlated demand and solar availability
randvar=rand(1,N+Nval); %generate a rand var to be used in solar and demand
d=20+25*(randvar+rand(1,N+Nval)); % this is the demand vector

% generate random solar availability
poff = 0.5; % no solar some of the time
punif = 0.3; % prob mass uniformly distributed on [0,1]
% otherwise, solar on full
f = 1/punif; g = -poff/punif;
asolar=f*randvar+g;
asolar = max(asolar,0);  % clip a to be >= 0
asolar = min(asolar,1); % clip a to be <= 1

% stack availabilities into one matrix
A=[acoal;awind;asolar];

% separate training and validation sets
dval=d(:,N+1:N+Nval);
d(:,N+1:N+Nval)=[];

Aval=A(:,N+1:N+Nval);
A(:,N+1:N+Nval)=[];

% clear place holder variables
clear f g poff punif randvar cmax_coal cmax_wind cmax_solar ...
    b_coal b_wind b_solar n_wind asolar awind acoal
