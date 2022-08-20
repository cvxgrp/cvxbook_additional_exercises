L = 1.5;
a = 1;
C = 15;
N = 200;
h = a/N;

F = [20,40,140,180]';
yfixed = zeros(N+1,1);
yfixed(20) = 0.1; 
yfixed(40) = 0.15; 
yfixed(140) = 0.15; 
yfixed(180) = 0.2;

% plot your curve using the following code
% plot the fixed points (don't modify)
% ----------------------------------------------
% x = [0:h:a];
% figure; hold on;
% plot(0,0,'bo','markerfacecolor','b','markersize',7);
% plot(a,0,'bo','markerfacecolor','b','markersize',7);
% for i = 1:length(F);
%     plot(x(F(i)),yfixed(F(i)),'bo',...
%            'markerfacecolor','b','markersize',7);
% end
% axis([0,1,0,0.4]);

% INSERT YOUR VARIABLES HERE:
% ----------------------------------------------
% plot(x,y);

