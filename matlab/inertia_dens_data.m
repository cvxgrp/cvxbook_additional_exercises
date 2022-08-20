% problem data for optimizing inertia over mass disitribution
a=1;  % pixel area
mgiven=1;  % total mass
n=25; % grid will be n x n
t = linspace(-1,1,n);
[x,y]=meshgrid(t,t);
x=x(:); y=y(:);
% define region
ind = max(abs(x-2/3),abs(y-2/3))> 1/3 & max(abs(x-1/3),abs(y+1/2)*3)>.45;
x=x(ind); y=y(ind);
Z = [x'; y'];
N = length(x);
rhomax=4*mgiven/N;  % max density is no more than 4 times uniform density

% replace below with your solution
rho = rand(N,1);

% plot
P = nan(n,n) ; P(ind)=rho;
pcolor(P); axis square;
colormap autumn; colorbar; 
