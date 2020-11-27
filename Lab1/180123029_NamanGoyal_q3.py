import pandas as pd
import matplotlib.pyplot as plt 

x_axis_vals=[]
y_axis_vals=[]

def plot_graph(a,b,m):
    seed=100
    val=seed
    for i in range(0,m+1):
        current_val=val
        val=(current_val*a+b)%m
        x_axis_vals.append(current_val/m)
        y_axis_vals.append(val/m)
        if(val==seed):
            break
            

#We observe that the graph does not change pattern by varying the value of seed;
a=1229
b=1
m=2048
plot_graph(a,b,m) # Giving values to the fun plot_graph
plt.scatter(x_axis_vals,y_axis_vals,s=5)
plt.title('Question_3 for any seed value')
plt.xlabel('X-axis ------------>')
plt.ylabel('Y-axis ------------>')
plt.show()
