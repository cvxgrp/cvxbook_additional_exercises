% data for approximate conformal mapping problem.
% generate boundary of original region to map
N = 360; % number of boundary sample points
theta = 2*pi*[1:N]/N;
r = 1+0.1*cos(theta)-0.15*sin(2*theta)+0.1*cos(3*theta);
b = r.*cos(theta)+i*r.*sin(theta); % boundary of region
n = 10; % degree of polynomial to optimize over
a = 0; % point in interior of region

subplot(1,2,1)
plot(real(b),imag(b));
title('Boundary of region');
axis equal;
axis ([-1.5 1.5 -1.5 1.5]);

% replace line below with optimal alpha
alpha = zeros(n+1,1);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% INSERT YOUR CODE HERE
% Solve the conformal mapping problem.
% Store your result in the variable alpha




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


w = polyval(alpha,b);  % (boundary of) mapped region

subplot(1,2,2)
plot(real(w),imag(w),'b',cos(theta),sin(theta),'g');
title('Boundary of mapped region');
axis equal;
axis ([-1.5 1.5 -1.5 1.5]);
