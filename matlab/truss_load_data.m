% data for truss load analysis problem

n = 9;  % total number of nodes (free + anchor)
m = 14; % number of bars
p = 6;  % number of free nodes

% limits on bar tensions
Tmin = -ones(m,1);
Tmax = ones(m,1);

%node locations (first p are free)
P = [ 2   2;
      2.5 3;
      5.4 2;
      0.5 4;
      3.6 2;
      3.2 3.2;
      3   1;
      1   1;
      5   0.5];
  
incidMat = ... % one row per bar; gives indices of nodes
    [1 2;
     1 4;
     1 7;
     1 8;
     2 4;
     2 6;
     2 8;
     3 5;
     3 6;
     3 9;
     4 8;
     5 6;
     5 9;
     6 7];

%project tensions onto nodes
A = zeros(2*n,m);
for i = 1:m
    direc = abs(P(incidMat(i,1),:) - P(incidMat(i,2),:));
    direc = direc/norm(direc);
    if (P(incidMat(i,1),1) >= P(incidMat(i,2),1))
        A(2*incidMat(i,1)-1,i) = -direc(1);
        A(2*incidMat(i,2)-1,i) = direc(1);
    else
        A(2*incidMat(i,1)-1,i) = direc(1);
        A(2*incidMat(i,2)-1,i) = -direc(1);
    end
    if (P(incidMat(i,1),2) >= P(incidMat(i,2),2))
        A(2*incidMat(i,1),i) = -direc(2);
        A(2*incidMat(i,2),i) = direc(2);
    else
        A(2*incidMat(i,1),i) = direc(2);
        A(2*incidMat(i,2),i) = -direc(2);
    end
end

%rearrange x,y components of f_load to be in correct places
A = [A(1:2:2*p-1,:); A(2:2:2*p,:); A(2*p+1:2*n,:)];

% The following code can be used to visualize the truss and is not
% necessary to solve this problem
 
Ad = zeros(n);
for i = 1:m
    Ad(incidMat(i,1), incidMat(i,2)) = 1;
end
Ad = Ad + Ad';
 
epsx = 0.05; epsy = 0.15; % text placing offset 

figure; 
 
gplot(Ad,P,'k-'); hold on;
axis([min(P(:,1))-0.5, max(P(:,1)) + 0.5, ...
     min(P(:,2))-0.5, max(P(:,2)) + 0.5])
 
% label free nodes
for j = 1:p
    plot(P(j,1),P(j,2),'.b',...
    'MarkerSize',15);
    
    text(P(j,1)-eps,P(j,2)+epsy,int2str(j),'FontSize',10);
end

% label anchor nodes 
for j = p+1:n
    plot(P(j,1),P(j,2),'rs',...
        'MarkerFaceColor','r',...
        'MarkerSize',12);
    text(P(j,1)-eps,P(j,2)+epsy,int2str(j),'FontSize',10);     
end

hold off;
