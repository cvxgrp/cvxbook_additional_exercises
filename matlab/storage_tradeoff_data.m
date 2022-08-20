randn('seed', 1); 
T = 96; % 15 minute intervals in a 24 hour period
t = (1:T)'; 
p = exp(-cos((t-15)*2*pi/T)+0.01*randn(T,1)); 
u = 2*exp(-0.6*cos((t+40)*pi/T) -0.7*cos(t*4*pi/T)+0.01*randn(T,1));
plot(t/4, p); 
hold on
plot(t/4,u,'r');