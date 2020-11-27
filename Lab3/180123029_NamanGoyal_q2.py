import numpy as np
import matplotlib.pyplot as plt
import statistics 
import math
import random as rand

values_c = [135/64,15,36];

def fun(x):
    return (20 * x * pow((1-x),3));
    
for val in values_c:
    count_arr = [];
    x_arr = [];
    for i in range(1000000):
        cur=0
        while(1):
            rand1=rand.random()
            rand2=rand.random()
            cur = cur+1
            if val*rand2 <= fun(rand1):
                x_arr.append(rand1)
                count_arr.append(cur)
                break
# Calculating the avg count of iterations.                
    print("Average count of iterations for "+ str(val)+ " = " , statistics.mean(count_arr))
    
    x_sp=np.linspace(0,1,250);
    new_fun = 1000000 * fun(x_sp)/250;
    
    plt.plot(x_sp,new_fun,color='blue');
    plt.hist(x_arr,bins=250,color = 'g')
    plt.plot()
    plt.xlabel('Values of the Random Numbers')
    plt.ylabel('Frequencies')
    plt.show()
