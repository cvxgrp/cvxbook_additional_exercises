% data for power flow problem

n = 11; % total number of nodes
m = 19; % number of edges (transmission lines)
k = 3;  % number of generators

rand('state',1);
Gmax  = [3; 5; 9];         % maximum generator power
a     = [10; 8; 3];        % generator linear costs
b     = [0.2; 0.3; 0.1];   % generator quadratic costs
l     = 1 + rand(n-k,1);   % network loads
R     = ones(m,1);         % initial assignment of conductor radii
Rmax  = 1.5*ones(m,1);     % maximum conductor radii
Rmin  = 0.5*ones(m,1);     % minimum conductor radii
alpha = 0.05;              % conductor loss coefficient
sigma = 4.5;                 % coeff for max line power

% graph incidence matrix
A = [ -1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;
       0  0  0  0  0  0  0  0  0 -1  0  0 -1  0  0 -1  0  0  0 ;
       0  0  0  0  0  0  0  0  0  0  0  0  0  0 -1  0  0  0 -1 ;
       0  0  0  0  1 -1  0  1 -1  0  1  1  0  0  0  0  1  0  0 ;
       1 -1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;
       0  1  1  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0 ;
       0  0  0  1  0  0  0 -1  0  1  0  0  0  0  0  0  0  0  0 ;
       0  0 -1  0  0  0  1  0  1  0  0  0  0  0  0  0  0  0  1 ;
       0  0  0  0  0  0  0  0  0  0 -1  0  1 -1  0  0  0 -1  0 ;
       0  0  0  0  0  0 -1  0  0  0  0 -1  0  1  1  0  0  0  0 ;
       0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1 -1  1  0 ];
   
% x-y coordinates
XY = [ ...  % node x-y coordinates
 1.2 4.8;   % node 1
 0.8 3.4;   % node 2
 6.7 2.7;   % node 3
 3.8 4.1;   % node 4
 3.2 4.8;   % node 5
 5.9 4.8;   % node 6
 1.8 4.1;   % node 7
 5.9 3.7;   % node 8
 3.5 2.7;   % node 9
 5.4 2.8;   % node 10
 2.8 3.5];  % node 11

%node distances
L = zeros(m,1);
idx = zeros(m,2);
for j = 1:m
    idx(j,1) = find(A(:,j) == 1);
    idx(j,2) = find(A(:,j) == -1);
    L(j) = norm(XY(idx(j,1),:) - XY(idx(j,2),:));
end

Vmax = L'*R.^2; %volume constraint

% the code below is not data for the problem
% it is used only to display the network graph

% Generators are represented by red squares, loads by blue circles.  An
% edge is oriented towards the node that is closer to the small, green
% square on that edge.  Nodes numbers are in plain text, edge numbers are
% in plain text inside a green box

% node adjacency matrix
Ad = -A*A';
Ad = Ad - diag(diag(Ad));

epsx = 0.05; epsy = 0.15; % text placing offset 

figure; 
% connect edges
gplot(Ad,XY,'-k'); hold on;

% label generator nodes
for j = 1:k
    plot(XY(j,1),XY(j,2),'rs',...
        'MarkerFaceColor','r',...
        'MarkerSize',12);
    text(XY(j,1)-eps,XY(j,2)+epsy,int2str(j),'FontSize',10);      
end

% label load nodes 
for j = k+1:n
    plot(XY(j,1),XY(j,2),'.b',...
    'MarkerSize',15);
    text(XY(j,1)-eps,XY(j,2)+epsy,int2str(j),'FontSize',10); 
end

%plot directions and edges
for i = 1:m
    x = XY(idx(i,1),1) - 1/6*(XY(idx(i,1),1) - XY(idx(i,2),1));
    y = XY(idx(i,1),2) - 1/6*(XY(idx(i,1),2) - XY(idx(i,2),2));
    plot(x,y,'rs',...
        'MarkerFaceColor','g',...
        'MarkerSize',5);
    xtxt = XY(idx(i,1),1) - 1/2*(XY(idx(i,1),1) - XY(idx(i,2),1));
    ytxt = XY(idx(i,1),2) - 1/2*(XY(idx(i,1),2) - XY(idx(i,2),2));
    text(xtxt-eps,ytxt+epsy,int2str(i),'FontSize',10,'BackgroundColor','g');
end
axis off; hold off;
