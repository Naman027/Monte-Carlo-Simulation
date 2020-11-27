import numpy as np
import time
import statistics
import math
import random
import matplotlib.pyplot as plt

Stock_Prices=[184.800003,185.449997,184.699997,188.050003,188.600006,191.899994,199.100006,195.600006,192.699997,186.050003,183.800003,186.25,188.199997,190.75,194.399994,192,198.25,191.949997,187.149994,189.449997,191.199997,186.550003,191.449997,192.25,191.600006,191.449997,190.949997,190.649994,193.800003,195.050003,203.300003,201.899994,196.5,193.100006,195.100006,197.050003,194.75,198.399994,201.449997,207.949997, 209.850006,215.649994,224.850006,212,218.100006,216.25,213.149994,206.600006,207.899994,204.050003,194.850006,198.149994,202.699997,198.5,200.149994,198.199997,195.449997,192.600006,185.800003,186.199997,183.800003,176.350006,182.199997,187.25,185.050003,185.399994]

def Univariate_Normal():
    u1= random.random()
    u2= random.random()
    r= -2*math.log(u1)
    theta= 2*math.pi*u2
    z1= math.sqrt(r)*math.cos(theta)
    return z1

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
print("The calculated value of Sigma = ", Sigma)
print("")

# S0 should be the price for 30th Sept
S0 = 185.399994
K= 1.1*S0
N=300
PayOFF_Asian = []
PayOFF_European = []
print("Average price Asian put option (in the BSM framework) ---> ")
for i in range(1000):
    Stock = S0
    X = []
    for i in range(301):
        Z = Univariate_Normal()
        Stock = Stock * math.exp((Mu - 0.5*(Sigma*Sigma))*0.1 + Sigma*Z*math.sqrt(0.1))
        X.append(Stock)
    Payoff_1 = max(0, K - (math.fsum(X)/301))
    PayOFF_Asian.append(Payoff_1)
    Payoff_1_European = max(0, K - X[299])
    PayOFF_European.append(Payoff_1_European)
Mean_Asian = statistics.mean(PayOFF_Asian)
Variance_Asian = statistics.variance(PayOFF_Asian)
Mean_European = statistics.mean(PayOFF_European)
Variance_European = statistics.variance(PayOFF_European)
print("Mean of the payoffs to an Asian put option is:",Mean_Asian)
print("Variance of the payoffs to an Asian put option is: ",Variance_Asian)
print("The 95% Confidence interval is [",Mean_Asian - (1.96 * math.sqrt(Variance_Asian))/ math.sqrt(1000),",",Mean_Asian + (1.96 * math.sqrt(Variance_Asian)) / math.sqrt(1000),"]")

cur = 0
for i in range(1000):
    cur+= (PayOFF_European[i] - Mean_European) * (PayOFF_Asian[i] - Mean_Asian)

covariance = cur / 1000
b = covariance/Variance_European
print(" ")
print("Using the control variate ---> ")
print("The Value of b: ",b)
Y = []
for i in range(1000):
    Stock = S0
    X = []
    for i in range(301):
        Z = Univariate_Normal()
        Stock = Stock * math.exp((Mu -0.5*(Sigma*Sigma))*0.1+ Sigma*Z*math.sqrt(0.1))
        X.append(Stock)
    PayOFF_Control = max(0, K - (math.fsum(X) / 301))
    PayOFF_Control_European = max(0, K - X[299])
    Val = PayOFF_Control - b * (PayOFF_Control_European - Mean_European)
    Y.append(Val)
Mean2 = statistics.mean(Y)
Variance2 = statistics.variance(Y)
print("Mean of the payoffs to an Asian put option is: ",Mean2)
print("Variance of the payoffs to an Asian put option is: ",Variance2)
print("The 95% Confidence interval is [",Mean2 - (1.96 * math.sqrt(Variance2))/ math.sqrt(1000),",",Mean2 + (1.96 * math.sqrt(Variance2)) / math.sqrt(1000),"]")
