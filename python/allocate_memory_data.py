import numpy as np
import matplotlib.pyplot as plt
Banks=[]
for i in range(0,16,1):
    for j in reversed(range(0,16,1)):
        Banks.append([i+0.5,j+0.5])
Cores=[[0,16],[8,16],[16,16],[0,8],[16,8],[0,0],[8,0],[16,0]]  
def Cost1(P1,P2):
    return np.linalg.norm(np.array(P1)-np.array(P2),ord=1)
def Cost2(P1,P2):
    return np.power(np.linalg.norm(np.array(P1)-np.array(P2),ord=1),3/2)
#----------------------------------------------------------------------
#Use problem the following problem data in your solution.
m=256#number of banks
n=8#number of cores
C=np.ones((n,m))
D=np.ones((n,m))
for i in range(n):
    for j in range(m):
        C[i,j]=Cost1(Cores[i],Banks[j])
        D[i,j]=0.01*Cost2(Cores[i],Banks[j])
c=32*np.ones((m,))#capacity of bank j
b=np.array([2048,1024,512,1024,1024,512,1024,512])#storage requirement of core i
#----------------------------------------------------------------------
#Use the following plotting function to plot your optimal memory allocation M
#You only need to input matrix an n-by-m matrix M.
#Assuming you find optimal memory allocation M, you can plot it and visualize the grid as:
#plot_memory(M)
def plot_memory(M, save_file="allocating_memory_py.pdf"):
    m=256#number of banks
    n=8#number of cores       
    Ratio={}
    for j in range(m):
        Ratio[j]=[]
        for i in range(n):
            Ratio[j].append(M[i,j]/32)    
    def y_line(index,x):
        return index*np.ones(len(x))
    def x_segment(index,xm):
        return xm[int(index*100):int((index+1)*100)]
    x=np.linspace(0,16,1600)
    xmain=np.linspace(0,16,1600)
    for i in range(17):
        y=y_line(i,x)
        plt.plot(x,y,"k")
        plt.plot(y,x,"k")
    colormap=["midnightblue","blue","turquoise","lime","yellow","orange","red","deeppink"]
    for banka in Ratio:
        row_number=15-banka//16
        column_number=banka%16
        r=Ratio[banka]#array of 8
        y_prev=(row_number)*np.ones((100,))
        sum_r_so_far=0.0
        for i in range(n):
            if r[i]>0.001:
                x=x_segment(column_number,xmain)
                y=(row_number+sum_r_so_far+r[i])*np.ones((100,))#
                plt.fill_between(x, y, y_prev,color=colormap[i])
                y_prev=y
                sum_r_so_far+=r[i]
    plt.scatter([0,8,16,0,16,0,8,16],[16,16,16,8,8,0,0,0],s=80,c='k')
    plt.axis('off')
    plt.show
    plt.savefig(save_file)


