%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GENERATES DATA, SHOULD NOT BE IN STUDENT VERSION

clear all; close all;

rand('state',0);
randn('state',0);

% Define edges of graph
n = 60;

A = rand(n,n) < 0.05;
prec = [];
for i = 1:n
    for j = (i+1):n
        if A(i,j) == 1
            prec = [prec; i j];
        end
    end
end
[m,k] = size(prec);

% Define workload in alpha
alpha = rand(n,1)*4+0.1;
 
% Define power function
s_min = 1; s_max = 5;

% ---------- write a ps_data.m--------------------------------------------
fid = fopen('ps_data.m','w');

fprintf(fid,'prec =[');
fprintf(fid,'%d %d; \n',prec(1,1),prec(1,2));
for i=2:m
    fprintf(fid,'       %d %d',prec(i,1),prec(i,2));
    if i < m
        fprintf(fid,'; \n');
    else
        fprintf(fid,'];\n');
    end
end
fprintf(fid,'\n');
fprintf(fid,'alpha =[');
fprintf(fid,'%1.4f; \n',alpha(1));
for i=2:n
    fprintf(fid,'        %1.4f',alpha(i));
    if i < n
        fprintf(fid,'; \n');
    else
        fprintf(fid,'];\n');
    end
end
fprintf(fid,'\n');
fprintf(fid,'n = %d; \n\n',n);
fprintf(fid,'m = %d; \n\n',m);
fprintf(fid,'s_min = %d; \n\n',s_min);
fprintf(fid,'s_max = %d; \n\n',s_max);
fclose(fid);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
