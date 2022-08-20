% data file for lightest structure problem
% m: number of nodes
% n: number of bars
% k: number of free nodes
% f: loading forces
% f(:, :, i) is a 2 x k matrix giving the forces for loading i
clear all;
rand('seed', 1);
randn('seed', 1);

N = 5; % number of fixed nodes
k = N*(N-1); % number of free nodes

[X, Y] = meshgrid(0:N-1, 0:N-1);
P = [Y(:)'; X(end:-1:1)];

m = length(P); % total number of nodes
r = []; s = [];

dx = [-1  0  1 1];
dy = [-1 -1 -1 0];
for ind = 1:m
    for i = 1:4
        px = P(1, ind) + dx(i);
        py = P(2, ind) + dy(i);
        if 0 <= px && px < N && 0 <= py && py < N
            r(end+1) = ind;
            s(end+1) = find(P(1, :)==px & P(2, :)==py);
        end
    end
end
n = length(r); % number of bars
sigma = 1;

M = 4; % number of loadings
F = zeros(2, k, M);
% load 1: (nominal) equal forces down
F(2, :, 1) = -2;

% load 2/3: nominal plus forces down-right and down-left
F(1, :, 2) =  rand(1, k);
F(1, :, 3) = -rand(1, k);
F(2, :, 2) = F(2, :, 1) - rand(1, k);
F(2, :, 3) = F(2, :, 1) - rand(1, k);

% load 4: nominal plus random forces in arbitrary directions
F(:, :, 4) = F(:, :, 1) + randn(2, k);

% use the code below to plot your solution
% dashed red lines indicate bars with zero (small) cross-sectional area
a = ones(n, 1); % replace 'a' with your solution

% plot
clf; hold on;
for i = 1:n
    p1 = r(i); p2 = s(i);
    plt_str = 'b-';
    width = a(i);
    if a(i) < 0.001
        plt_str = 'r--';
        width = 1;
    end
    plot([P(1, p1) P(1, p2)], [P(2, p1) P(2, p2)], ...
         plt_str, 'LineWidth', width);
end
axis([-0.5 N-0.5 -0.1 N-0.5]); axis square; box on;
set(gca, 'xtick', [], 'ytick', []);

clear X Y dx dy ind px py plt_str p1 p2 i a;
