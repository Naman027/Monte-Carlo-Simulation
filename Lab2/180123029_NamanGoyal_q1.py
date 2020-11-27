import pandas as pd
import random as rand
import matplotlib.pyplot as plt

a=1549
b=3
c=6144
seed=394
def finding_LCG(rounds,graph,bar_graph):
	x_axis_values = []
	y_axis_values = []
	xinit = (a*seed + b)%m
	uinit = xinit/m
	for i in range (17):
		x_axis_values.append(uinit)
		xinit = (a * xinit + b) % m
		uinit = xinit / m
		y_axis_values.append(uinit)

	for i in range (rounds):
		x_axis_values.append(uinit)
		uinit = x_axis_values[i-17] - x_axis_values[i-5]
		if uinit<0:
			uinit = uinit+1
		y_axis_values.append(uinit)		

	plt.figure(figsize=(10,9))
	plt.title("Values of U(i) and U(i+1) for %s rounds" % rounds, fontsize=16)
	plt.xlabel("U(i) Values", fontsize=16)
	plt.ylabel("U(i+1) Values", fontsize=16)
	plt.scatter(x_axis_values, y_axis_values)
	plt.savefig(graph)
	plt.clf()	

	plt.figure(figsize=(10,9))
	plt.title("Bar Graph of Frequencies of U(i) values for %s rounds" % rounds, fontsize=16)
	plt.xlabel("U(i) Intervals", fontsize=16)
	plt.ylabel("Corresponding Frequency", fontsize=16)
	plt.hist(x_axis_values, edgecolor='black')
	plt.savefig(bar_graph)
	plt.clf()	

# Passing the values to the functions

p1 = "Q1_Graph_1st for rounds = 1000"
p2 = "Q1_Bar_Graph_1st for rounds = 1000"
finding_LCG(1000,p1,p2)

p1 = "Q1_Graph_2nd for rounds = 10000"
p2 = "Q1_Bar_Graph_2nd for rounds = 10000"
finding_LCG(10000,p1,p2)

p1 = "Q1_Graph_3rd for rounds = 100000"
p2 = "Q1_Bar_Graph_3rd for rounds = 100000"
finding_LCG(100000,p1,p2)
