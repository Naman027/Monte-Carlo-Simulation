import csv
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph_frequencies(a,m):
    freq=['-1']
    it=0
    while it<100:
        freq.append(str(it/100)+'-'+str((it+5)/100))
        it+=5
        
    values_x0=[151668,185005,120896,20521,23700]
    bar_graph=[]
    for i in values_x0:
        new_bar_graph=[]
        length=len(freq)-1
        map_freq=[0]*(length)
        x=(a*i)%m
        ui=x/m
        for j in range(10*m):
            cur_val=0;
            if (100*ui)%5==0:
            	cur_val=(100*ui)/5
            else :
            	cur_val= (100*ui)/5-1;
            map_freq[int(cur_val)]=map_freq[int(cur_val)]+1
            new_bar_graph.append(ui)
            x=(a*x)%m
            ui=x/m
            
        data_frame = pd.DataFrame({
        'x0='+str(i): new_bar_graph,
        'a='+str(a): new_bar_graph
        })
        bar_graph = data_frame.plot.hist(bins=20,rwidth=0.6)

plot_graph_frequencies(1597,244944)
plot_graph_frequencies(51749,244944)

