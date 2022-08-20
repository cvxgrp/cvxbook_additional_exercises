raw = im2double(imread('demosaic_raw.png', 'png'));
[m, n, ~] = size(raw);

% Set up matrix masks
R_mask = false(m, n);
G_mask = false(m, n);
B_mask = false(m, n);
R_mask(1:2:n, 1:2:m) = true;
G_mask(2:2:n, 1:2:m) = true;
G_mask(1:2:n, 2:2:m) = true;
B_mask(2:2:n, 2:2:m) = true;

% Load data into respective matrices by setting the irrelevant indices to 0
R_raw = raw(:,:,1);
G_raw = raw(:,:,2);
B_raw = raw(:,:,3);

clear raw;

% Use this function to display and save the R, G, B matrices computed as an
% image
function save_image(R, G, B, output_filename)
    if nargin < 4
        output_filename = 'output_image.png';
    end
    img = cat(3, R, G, B);
    image(img); % show image
    imwrite(img, output_filename);
end
