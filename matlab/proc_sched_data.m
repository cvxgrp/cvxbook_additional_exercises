% EE364a final 2008.
% Data for minimum energy processor speed scheduling.

n = 12;  % number of jobs.
T = 16;  % number of time periods.

Smin = 1;  % min processor speed.
Smax = 4;  % max processor speed.
R = 1;  % max slew rate.

% Parameters in power/speed model.
alpha = 1;
beta = 1;
gamma = 1;

% Job arrival times and deadlines.
A = [1; 3;  4; 6; 9;  9; 11; 12; 13; 13; 14; 15];
D = [3; 6; 11; 7; 9; 12; 13; 15; 15; 16; 14; 16];
% Total work for each job.
W = [2; 4; 10; 2; 3; 2; 3; 2; 3; 4; 1; 4];

% Plot showing job availability times & deadlines.
figure;
hold on;
scatter(A,[1:n],'k*');
scatter(D+1,[1:n],'ko');
for i=1:n
    plot([A(i),D(i)+1],[i,i],'k-');
end
hold off;
xlabel('time t');
ylabel('job i');

