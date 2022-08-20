% Least-cost road grading.

n = 100;
e = 5*sin((1:n)/n*3*pi)'+sin((1:n)/n*10*pi)';% elevation of the road
d = 1; % distance between points
D1 = .08; % the road grade should never be greater than 8%
D2 = .025; % the road grade should never change faster than 25% over 10 meters
D3 = .005; % a further constraint on the smoothness of the road.

% cut and fill function coefficients of the form alpha*x_+^2+beta*x_+
alpha_fill = 2;
beta_fill = 30;
alpha_cut = 12;
beta_cut = 1;

% a plot of the cost functions
figure
elevation = 0:.1:10;
plot(elevation,alpha_fill*elevation.^2+beta_fill*elevation,'b');
hold on
plot(elevation,alpha_cut*elevation.^2+beta_cut*elevation,'g');
xlabel('elevation change')
ylabel('cost')
legend('fill','cut')

print -depsc road_grading_cost_function.eps

h = ones(n,1)*mean(e); % replace h with your solution.

figure
subplot(2,1,1)
plot((0:n-1)*d,e,'--r');
ylabel('elevation');
hold on
plot((0:n-1)*d,h, 'b')
legend('e','h');
subplot(2,1,2)
plot((0:n-1)*d,h-e)
ylabel('elevation change')
xlabel('distance')
