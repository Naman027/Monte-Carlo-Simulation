import math
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import matplotlib
import statistics
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def f(x,mu,std):
    return (1/(std*math.sqrt(2*math.pi))*(np.exp(-0.5*(x-mu)*(x-mu)/(std*std))));
    
def generate(a,sigma):
    x1=[0]*1000;
    x2=[0]*1000;
    y1=[0]*1000;
    y2=[0]*1000;
    i=0
    while(i<1000):
        u1=random.random()
        u2=random.random()
        u1=2*u1-1
        u2=2*u2-1
    	
        cur = u1*u1+u2*u2
        if cur<=1:
    	    y = math.sqrt(-2*math.log(cur)/cur)
    	    y1[i]=u1*y;
    	    y2[i]=u2*y;
    	    i+=1
   
    for j in range(1000):
        x1[j]=5+y1[j];
        x2[j]=8+2*a*y1[j]+(math.sqrt(1 - (a*a))*2)*y2[j];
        
    plt.figure(figsize=(5,5))     
    plt.hist(x1,bins=30, color='blue', ec='black');
    plt.xlabel("Marginal X1 ---->")
    plt.ylabel("Frequencies ")
    np_x=np.array(x1);
    X=np.linspace(min(np_x),max(np_x),300);
    Y=(1000)*f(X, 5, 1)*(max(np_x)-min(np_x))/30;
    plt.plot(X, Y, color='r');
    plt.show();
    
    plt.figure(figsize=(5,5)) 
    plt.hist(x2,bins=30, color='blue', ec='black');
    plt.xlabel("Marginal X2 --->")
    plt.ylabel("Frequencies")
    np_x=np.array(x2);
    X=np.linspace(min(np_x),max(np_x), 300);
    Y=(1000)*f(X, 8, 2)*(max(np_x)-min(np_x))/30;
    plt.plot(X, Y, color='r');
    plt.show();
    fig = plt.figure()
    
    
    ax = fig.add_subplot(111, projection='3d')
    hist,xedges,yedges=np.histogram2d(x1,x2,bins=30,range=[[min(x1),max(x1)],[min(x2),max(x2)]])
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos=xpos.ravel()
    ypos=ypos.ravel()
    zpos=0
    dx=dy=0.5*np.ones_like(zpos)
    dz = hist.ravel()
    ax.bar3d(xpos,ypos,zpos,dx,dy,dz,zsort='average')
    ax.set_xlabel("X1 -->");
    ax.set_ylabel("X2 -->");
    ax.set_zlabel("Frequency -->");
    print("3D Histogram for a=", str(a));
    plt.show()
    
    # for a=1 1-a*a= 0
    if a==1:
        a=0.95
        
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.linspace(min(x1), max(x1),1000)
    Y = np.linspace(min(x2), max(x2),1000)
    X,Y = np.meshgrid(X, Y)
    p = (4*(X-5)*(X-5) - 4*a*(X-5)*(Y-8) + (Y-5)*(Y-8))/(8*(a*a-1));
    Z = (1/(4*np.pi*(math.sqrt(1-a*a))))*np.exp(p);
    s = ax.plot_surface(X ,Y, Z, cmap=cm.coolwarm,linewidth=0)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(s, shrink=0.5, aspect=5)
    print("Expected surface 3d for a = ", str(a));
    plt.show()

variance =[[1,(2*(-0.5))],[(2*(-0.5)),4]];
print("a=",-0.5);
generate(-0.5,variance)

variance =[[1,(2*(0))],[(2*0),4]];
print("a=",0);
generate(0,variance)

variance =[[1,(2*(0.5))],[(2*0.5),4]];
print("a=",0.5);
generate(0.5,variance)

variance =[[1,(2*(1))],[(2*1),4]];
print("a=",1);
generate(1,variance)
