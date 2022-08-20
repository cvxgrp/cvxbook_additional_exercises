% radiation treatment planning data file
% this one is randomly generated; a real one would use the beam geometry
rand('state',0);
n = 200; % number of beams
mtarget = 100; % number of tumor or target voxels
mother = 400; % number of other voxels
Atarget = sprand(mtarget,n,0.2);
Atarget = Atarget + [5*sprand(mtarget,mtarget,0.2) zeros(mtarget,n-mtarget)];
Aother= sprand(mother,n,0.2);
Bmax = 10;
Dtarget = 1;
Dother = 0.2;
