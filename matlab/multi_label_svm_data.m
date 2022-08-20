% data file for multi-label SVM problem
clear all;
randn('state', 0);
mTrain = 1000; % size of training data
mTest  = 100;  % size of test data
K = 10;        % number of categories
n = 20;        % number of features
A_true = randn(K, n);
b_true = randn(K, 1);
v = 0.2*randn(K, mTrain + mTest); % noise
data = randn(n, mTrain + mTest);    
[~, label] = max(A_true * data + b_true * ones(1, mTrain + mTest) + v, [], 1);
% training data
x = data(:, 1:mTrain);
y = label(1:mTrain);
% test data
xtest = data(:, (mTrain+1):end);
ytest = label((mTrain+1):end);