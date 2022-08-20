function r = ranking_est_data(y)
% Returns the rakning of the argument.
% :param y: a 2d array of size N x K or a 1d array of size K, 
% input vector or N vectors to generate the rankings
% :return: a 2d array with ith row being the ranking of the ith row 
% of y if y is a 2d array, and a 1d ranking if y is a 1d array
    if ndims(y) == 1
        [~,r]=sort(y);
        [~,r]=sort(r);
    else
        [~,r]=sort(y, 2);
        [~,r]=sort(r, 2);
    end
end
