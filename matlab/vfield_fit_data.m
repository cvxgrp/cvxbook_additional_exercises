%generate data for directional vector field fitting problem.
randn('state',0);
N=100; %should be a square.
[X1,X2]=meshgrid(linspace(-1,1,sqrt(N)),linspace(-1,1,sqrt(N)));
x1=X1(:)';
x2=X2(:)';
X=[x1;x2];
Atrue=[.1 1;-1 -.2];
btrue=[1;1];
Ftrue=Atrue*X+btrue*ones(1,N)+0.6*[max(X); min(X)];
Q=Ftrue*diag(1./norms(Ftrue));
%Let's plot the directions Q
quiver(x1,x2,Q(1,:),Q(2,:))
%Uncomment below to plot your normalized vector field
%Columns of Fhatn are columns of Fhat, scaled to have norm 1.
%hold on
%quiver(x1,x2,Fhatn(1,:),Fhatn(2,:),'r')
xlabel('x1')
ylabel('x2')
