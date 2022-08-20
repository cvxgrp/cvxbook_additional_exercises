rng(0); % 5
% read in image
im = im2double(imread('flower.png'));
[m,n,~] = size(im);
known_ind = find(rand(m,n) >= 0.90);
% grayscale image
M = 0.299*im(:,:,1)+0.587*im(:,:,2)+0.114*im(:,:,3);
% known color values
R_known = im(:,:,1);
G_known = im(:,:,2);
B_known = im(:,:,3);
R_known = R_known(known_ind);
G_known = G_known(known_ind);
B_known = B_known(known_ind);
% create damaged image
given_R = M;
given_R(known_ind) = R_known;
given_B = M;
given_B(known_ind) = B_known;
given_G = M;
given_G(known_ind) = G_known;
given = cat(3,given_R,given_G,given_B);
clear given_R given_B given_G;
% show original and damaged images
subplot(1,2,1);
subimage(im);
title('Original');
axis off;
subplot(1,2,2);
subimage(given);
title('Given');
axis off;
figure;
