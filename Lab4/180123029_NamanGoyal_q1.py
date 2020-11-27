import math
import matplotlib.pyplot as plt
import statistics
import random
import numpy as np
op=0

def generate(a1,a2):
	max_x = (a1-1)/(a1+a2-2)
	max_y = (math.gamma(a1+a2))*(max_x**(a1-1))*((1-max_x)**(a2-1))/(math.gamma(a1)*math.gamma(a2))
	
	c=max_y
	values=[]
	valx=[]
	x=0
	for i in range(100000):
		u=random.uniform(0,1)
		v=random.uniform(0,1)
		x=x+1
		if c*u<=(math.gamma(a1+a2))*(v**(a1-1))*((1-v)**(a2-1))/(math.gamma(a1)*math.gamma(a2)):
			values.append(round(v,5))
			valx.append(x)
			x=0
		
	avg_x = statistics.mean(valx)
	avg_y = statistics.mean(values)
	
	blocks_x=[]
	cur=0.01
	for i in range(100):
		blocks_x.append(round(cur,2))
		cur=cur+0.01

	ans=[0]*100
	for i in values:
		for j in range(100):
			if (i <= blocks_x[j]):
				ans[j] = ans[j] + 1
				break
				
	for i in range(100):
		ans[i]=ans[i]*100/len(values)
		
	plt.figure(figsize=(20,12))
	plt.title("Generated Frequencies: \n Value of (a1,a2) = (%s,%s) \n Value of x* = %s \n Value of c = %s \n " %(a1,a2,max_x,c),fontsize=15)
	
	
	plt.ylabel("Frequencies ---->",fontsize=20)
	plt.xlabel("X-Values ---->", fontsize=20)
	plt.bar(blocks_x,ans,width=0.01,edgecolor='black',color='lightblue')
	
	line_x = np.linspace(0,1,5000,endpoint=True)
	line_y = []
	for i in range(5000):
		cur_y =  (math.gamma(a1+a2))*(line_x[i]**(a1-1))*((1-line_x[i])**(a2-1))/(math.gamma(a1)*math.gamma(a2))
		line_y.append(cur_y)
	
	plt.plot(line_x,line_y,color='k')
	plt.savefig("Fig_No:" +str(op))
	plt.clf()
	
	
generate(1,5)
op = 1
generate(5,1)
op = 2
generate(2,3)
op = 3
generate(3,2)
op = 4
generate(3,3)


