import numpy as np
import time
import statistics
import math
import random
import matplotlib.pyplot as plt

L1 = []
L2 = []

# Without using Antithetic variables
print("For Sample Size = 100")
X = []
for i in range(100):
    U = np.random.uniform(0,1)
    X.append(math.exp(math.sqrt(U)))
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/100),",",mean + 1.96 * math.sqrt(variance/100),"]")
L1.append(2*1.96*math.sqrt(variance/100))
print("")
print("For Sample Size = 1000")
X = []
for i in range(1000):
    U = np.random.uniform(0,1)
    X.append(math.exp(math.sqrt(U)))
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/1000),",",mean + 1.96 * math.sqrt(variance/1000),"]")
L1.append(2*1.96*math.sqrt(variance/1000))
print("")
print("For Sample Size = 10000")
X = []
for i in range(10000):
    U = np.random.uniform(0,1)
    X.append(math.exp(math.sqrt(U)))
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/10000),",",mean + 1.96 * math.sqrt(variance/10000),"]")
L1.append(2*1.96*math.sqrt(variance/10000))
print("")
print("For Sample Size = 100000")
X = []
for i in range(100000):
    U = np.random.uniform(0,1)
    X.append(math.exp(math.sqrt(U)))
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/100000),",",mean + 1.96 * math.sqrt(variance/100000),"]")
L1.append(2*1.96*math.sqrt(variance/100000))
print("")

# Using Antithetic Variables
print("---------------------- Using Antithetic variables ------------------------------------------- ")
print("For Sample size = 100")
X = []
for i in range(100):
    U = np.random.uniform(0,1)
    X.append((math.exp(math.sqrt(U)) + math.exp(math.sqrt(1-U)))/2)
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/100),",",mean + 1.96 * math.sqrt(variance/100),"]")
L2.append(2*1.96*math.sqrt(variance/100))
print("")
print("For Sample size = 1000")
X = []
for i in range(1000):
    U = np.random.uniform(0,1)
    X.append((math.exp(math.sqrt(U)) + math.exp(math.sqrt(1-U)))/2)
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/1000),",",mean + 1.96 * math.sqrt(variance/1000),"]")
L2.append(2*1.96*math.sqrt(variance/1000))
print("")
print("For Sample size = 10000")
X = []
for i in range(10000):
    U = np.random.uniform(0,1)
    X.append((math.exp(math.sqrt(U)) + math.exp(math.sqrt(1-U)))/2)
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/10000),",",mean + 1.96 * math.sqrt(variance/10000),"]")
L2.append(2*1.96*math.sqrt(variance/10000))
print("")
print("For Sample size = 100000")
X = []
for i in range(100000):
    U = np.random.uniform(0,1)
    X.append((math.exp(math.sqrt(U)) + math.exp(math.sqrt(1-U)))/2)
mean = statistics.mean(X)
variance = statistics.variance(X)
print("Mean of this sample is",mean)
print("Variance of this sample is",variance)
print("The 95% Confidence interval is [",mean - 1.96 * math.sqrt(variance/100000),",",mean + 1.96 * math.sqrt(variance/100000),"]")
L2.append(2*1.96*math.sqrt(variance/100000))
print("")
print("Ratios of the lengths for the 95% Confidence intervals are --> ")
print("For sample size = 100   , the ratio is :",L1[0]/L2[0])
print("For sample size = 1000  , the ratio is :",L1[1]/L2[1])
print("For sample size = 10000 , the ratio is :",L1[2]/L2[2])
print("For sample size = 100000, the ratio is :",L1[3]/L2[3])

