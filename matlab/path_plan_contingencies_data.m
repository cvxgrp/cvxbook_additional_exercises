% parameters
N = 120;
O = 60;
S = 30;
h = 0.5;
p1 = 0.3; p2 = 0.3;
pN_1 = 0.3; pN = 0.3;

%%% FEEL FREE TO COPY THE FOLLOWING PLOTTING CODE ### 
% fig = figure(1); 
% x = (1 : N) * h;
% xlim([x(1), x(N)]);
% plot([S * h, S * h], [-1, 1], 'k--'); hold on;
% plot(x, P(:, 1), 'r', 'Linewidth', 2);
% plot(x, P(:, 2), 'b', 'LineWidth', 2);
% plot(x, P(:, 3), 'g', 'LineWidth', 2);
% plot([O * h, O * h], [0.5, 1], 'r--');
% plot([O * h, O * h], [-1, -0.5], 'b--');
% legend('obstacle revealed', 'obstacle left', ...
%     'obstacle right', 'obstacle clear', ...
%     'left safe region', 'right safe region');
% hold off;
% print(fig, '-depsc', 'path_plan_contingencies.eps');