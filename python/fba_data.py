# data file for flux balance analysis in systems biology
# From Segre, Zucker et al "From annotated genomes to metabolic flux
# models and kinetic parameter fitting" OMICS 7 (3), 301-316. 
import numpy as np

# Stoichiometric matrix
#	columns are M1	M2	M3	M4	M5	M6	
# For your interest, the rows correspond to the following equations
#	R1:  extracellular -->  M1
#	R2:  M1 -->  M2
#	R3:  M1 -->  M3
#	R4:  M2 + M5 --> 2 M4
#	R5:  extracellular -->  M5
#	R6:  2 M2 -->  M3 + M6
#	R7:  M3 -->  M4
#	R8:  M6 --> extracellular
#	R9:  M4 --> cell biomass
S = np.matrix("""
	1,0,0,0,0,0;
	-1,1,0,0,0,0;
	-1,0,1,0,0,0;
	0,-1,0,2,-1,0;
	0,0,0,0,1,0;
	0,-2,1,0,0,1;
	0,0,-1,1,0,0;
	0,0,0,0,0,-1;
	0,0,0,-1,0,0
	""").T
m,n = S.shape

vmax = np.matrix("""
	10.10;
	100;
	5.90;
	100;
	3.70;
	100;
	100;
	100;
	100
	""")
