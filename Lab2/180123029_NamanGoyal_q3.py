import pandas as pd
import numpy as np
import random 
import math
import matplotlib.pyplot as plt

def Function(theta,count_table,intervals,rounds,p):
	x_axis_values = []
	for i in range (rounds):
		cur_val = random.uniform(0,1)
		xinit = -1*theta*math.log(1-cur_val)
		x_axis_values.append(xinit)
		cur_val = 0.05
		for i in range(101):
			if (xinit <= cur_val):
				count_table[i] += 1	
			cur_val = round(cur_val + 0.05, 2)	
			
	mean = round(np.mean(x_axis_values), 5)
	variance = round(np.var(x_axis_values), 5)		
	plt.figure(figsize=(20,11))
	plt.xlabel("Intervals Range", fontsize=20)
	plt.ylabel("U(i)'s Cummulative Frequencies in given range", fontsize=20)
	plt.xticks(intervals, rotation='vertical')
	plt.title("Frequency Distribution Function\n Sample Mean = %s -> Actual Mean = 0.8 \n Sample Variance = %s -> Actual Variance = 0.64\n Number of Rounds during Simulation = %s" % (mean, variance,rounds), fontsize=20)
	plt.plot(intervals, count_table)
	plt.savefig(p)
	plt.clf()		

intervals_ranges = []
count_table = []
cur = 0.00
for i in range(101):
	intervals_ranges.append(cur)
	cur =  cur+ 0.05
	count_table.append(0)
# choosing theta variable
theta = 0.8
Function(theta,count_table,intervals_ranges,1000,"Cumulative Distributive Function for rounds = 1000")
#function F(x)
x = np.linspace(0, 10, 1000)
y = (2/np.pi)*(np.arcsin(np.sqrt(x)))

plt.figure(figsize=(20,11))
plt.xlabel("Range of Intervals", fontsize=20)
plt.ylabel("U(i)'s Cummulative Frequencies in given range", fontsize=22)
plt.scatter(x,y)
plt.savefig("Distribution for rounds = 1000")
plt.clf()

Function(theta,count_table,intervals_ranges,10000,"Cumulative Distributive Function for rounds = 10000")
#function F(x)
x = np.linspace(0, 10, 1000)
y = (2/np.pi)*(np.arcsin(np.sqrt(x)))

plt.figure(figsize=(20,11))
plt.xlabel("Range of Intervals", fontsize=20)
plt.ylabel("U(i)'s Cummulative Frequencies in given range", fontsize=22)
plt.scatter(x,y)
plt.savefig("Distribution for rounds = 10000")
plt.clf()

Function(theta,count_table,intervals_ranges,100000,"Cumulative Distributive Function for rounds = 100000")
#function F(x)
x = np.linspace(0, 10, 1000)
y = (2/np.pi)*(np.arcsin(np.sqrt(x)))

plt.figure(figsize=(20,11))
plt.xlabel("Range of Intervals", fontsize=20)
plt.ylabel("U(i)'s Cummulative Frequencies in given range", fontsize=22)
plt.scatter(x,y)
plt.savefig("Distribution for rounds = 100000")
plt.clf()
