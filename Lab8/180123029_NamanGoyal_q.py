import numpy as np
import time
import statistics
import math
import random
import matplotlib.pyplot as plt

Stock_Prices=[184.800003,185.449997,184.699997,188.050003,188.600006,191.899994,199.100006,195.600006,192.699997,186.050003,183.800003,186.25,188.199997,190.75,194.399994,192,198.25,191.949997,187.149994,189.449997,191.199997,186.550003,191.449997,192.25,191.600006,191.449997,190.949997,190.649994,193.800003,195.050003,203.300003,201.899994,196.5,193.100006,195.100006,197.050003,194.75,198.399994,201.449997,207.949997, 209.850006,215.649994,224.850006,212,218.100006,216.25,213.149994,206.600006,207.899994,204.050003,194.850006,198.149994,202.699997,198.5,200.149994,198.199997,195.449997,192.600006,185.800003,186.199997,183.800003,176.350006,182.199997,187.25,185.050003,185.399994]

Z = []
n = len(Stock_Prices)
for i in range(n-1):
	Z.append(np.log(Stock_Prices[i+1]/Stock_Prices[i]))

cur = 0
n = len(Z)
for i in range(n):
	cur += Z[i]
Mu = cur/n

cur = 0
for i in range(n):
	cur += (Z[i]-Mu)*(Z[i]-Mu)
	
Sigma = cur/(n-1)
Mu_actual = Mu + Sigma/2
Mu = Mu_actual
Sigma = math.sqrt(Sigma)

print("The calculated value of mean = ", Mu)
print("The calculated value of variance = ", Sigma)

# S0 should be the price for 30th Sept
S0 = 185.399994

# for calculating the lognormal function
def fun(N):
	val = 0
	for i in range(N):
		val += (Mu + Sigma*np.random.normal(0,1,1)[0])
	return val

# for lambda = 0.01
print("For Lambda = 0.01")
Stock1 = []
S = S0
for i in range(1000):
	Z = np.random.normal(0,1,1)[0]
	N = np.random.poisson(0.01,1)[0]
	if N == 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z)
		Stock1.append(S)
	if N != 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z + fun(N))
		Stock1.append(S)

plt.plot(Stock1)
plt.title("Plot of Stock Price for Lambda = 0.01")
plt.xlabel("time (t)")
plt.ylabel("Stock Price S(t)")
plt.show()

# for labmda = 0.05
print("For Lambda = 0.05")
Stock2 = []
S = S0
for i in range(1000):
	Z = np.random.normal(0,1,1)[0]
	N = np.random.poisson(0.05,1)[0]
	if N == 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z)
		Stock2.append(S)
	if N != 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z + fun(N))
		Stock2.append(S)

plt.plot(Stock2)
plt.title("Plot of Stock Price for Lambda = 0.05")
plt.xlabel("time (t)")
plt.ylabel("Stock Price S(t)")
plt.show()

# for labmda = 0.1
print("For Lambda = 0.1")
Stock3 = []
S = S0
for i in range(1000):
	Z = np.random.normal(0,1,1)[0]
	N = np.random.poisson(0.1,1)[0]
	if N == 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z)
		Stock3.append(S)
	if N != 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z + fun(N))
		Stock3.append(S)

plt.plot(Stock3)
plt.title("Plot of Stock Price for Lambda = 0.1")
plt.xlabel("time (t)")
plt.ylabel("Stock Price S(t)")
plt.show()

# for labmda = 0.2
print("For Lambda = 0.2")
Stock4 = []
S = S0
for i in range(1000):
	Z = np.random.normal(0,1,1)[0]
	N = np.random.poisson(0.2,1)[0]
	if N == 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z)
		Stock4.append(S)
	if N != 0:
		S = S*math.exp((Mu - 0.5*Sigma*Sigma) + Sigma* Z + fun(N))
		Stock4.append(S)

plt.plot(Stock4)
plt.title("Plot of Stock Price for Lambda = 0.2")
plt.xlabel("time (t)")
plt.ylabel("Stock Price S(t)")
plt.show()















