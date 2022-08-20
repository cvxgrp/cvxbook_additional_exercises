% instance of hybrid vehicle optimization problem,
% exercise 4.65 in Boyd & Vandenberghe, Convex Optimization

% fuel use is given by F(p) = p+ gamma*p^2 (for p>=0)

% define Preq, required power at wheels
% Preq is piecewise linear
% a is slope of each piece
a=[0.5 -0.5 0.2 -0.7 0.6 -0.2 0.7 -0.5 0.8 -0.4];
% l is length of each piece
l=[40 20 40 40 20 40 30 40 30 60];

Preq=(a(1):a(1):a(1)*l(1))';
for i=2:length(l)
    Preq=[Preq; (Preq(end)+a(i):a(i):Preq(end)+a(i)*l(i))'];
end
% plot required power
plot(Preq)
xlabel('time'); ylabel('Preq'); title('Required power');

% problem parameters
T=sum(l);
Peng_max=20;
Pmg_min=-6;
Pmg_max=6;
Ebatt_max=100;
eta=0.1;
gamma=0.1;
