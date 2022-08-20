% data and code for multiperiod portfolio rebalancing problem
T = 100;
n = 5;
gamma = 8.0;
threshold = 0.001;
Sigma = [[  1.512e-02,  1.249e-03,  2.762e-04, -5.333e-03, -7.938e-04],
 [  1.249e-03,  1.030e-02,  6.740e-05, -1.301e-03, -1.937e-04],
 [  2.762e-04,  6.740e-05,  1.001e-02, -2.877e-04, -4.283e-05],
 [ -5.333e-03, -1.301e-03, -2.877e-04,  1.556e-02,  8.271e-04],
 [ -7.938e-04, -1.937e-04, -4.283e-05,  8.271e-04,  1.012e-02]];
mu = [ 1.02 , 1.028, 1.01 , 1.034, 1.017];
kappa_1 = [ 0.002, 0.002, 0.002, 0.002, 0.002];
kappa_2 = [ 0.004, 0.004, 0.004, 0.004, 0.004];

% Generate returns
% call this function to generate a vector r of market returns
generateReturns = @() mu + randn(1, length(mu)) * chol(Sigma);

% Plotting code
% You must provide three objects:
% - ws: matrix of size T x n,
%       the post-trade weights w_t_tilde;
% - us: matrix of size T x n, 
%       the trades at each period: w_t_tilde - w_t;
% - w_star: matrix of size n x 1,
%       the "target" solution w_star.
figure('position', [0, 0, 900, 400]);
colors = ['b','r','g','c','m'];
range = 1:T;
for j = 1:n
   hold on 
   plot(range, ws(:,j), ['-' colors(j)]);
   plot(range, ones(T)*w_star(j), ['--' colors(j)]);
   non_zero_trades = abs(us(:,j)) > threshold;
   plot(range(non_zero_trades), ws(non_zero_trades,j), ...
       ['o' colors(j)], 'MarkerFaceColor', colors(j));
end
xlabel('Period t');
ylabel('Post-trade weights');
