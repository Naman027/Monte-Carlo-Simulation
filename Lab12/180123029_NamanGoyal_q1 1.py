import numpy as np
import time
import statistics
import math
import random
import matplotlib.pyplot as plt

def calc_inverse(k,b):
    ans = 0.0
    po = 1.0
    while(k > 0):
        k,p = divmod(k, b)
        po *= b
        ans += p/po
    return ans

VanderCorput_25vals = []
for i in range(25):
    VanderCorput_25vals.append(calc_inverse(i,2))
print("------------------------------------------------------------------------------------------------------------------")
print("The first 25 values are: ")
print(VanderCorput_25vals)
print("------------------------------------------------------------------------------------------------------------------")
print("2D plot of pairs (xᵢ, xᵢ₊₁) for the first 1000 values of the sequence: ")
VanderCorput_1000vals_i = []
VanderCorput_1000vals_i1 = []
for i in range(1000):
    VanderCorput_1000vals_i.append(calc_inverse(i,2))
    VanderCorput_1000vals_i1.append(calc_inverse(i + 1,2))
plt.scatter(VanderCorput_1000vals_i,VanderCorput_1000vals_i1)
plt.axis([0, 1, 0, 1])
plt.title("Plot of pairs (xᵢ, xᵢ₊₁)")
plt.show()

print("------------------------------------------------------------------------------------------------------------------")
print("Sampled Distribution Plot of first 100 values using Vander Corput Sequence : ")
Y_100 = []
for i in range(100):
    Y_100.append(calc_inverse(i,2))
plt.hist(Y_100,density=True,bins=30,rwidth = 0.8)
plt.title("Distribution Plot for first 100 values using Vander Corput Sequence")
plt.show()

print("Linear Confruence Generator used : m = 4294967296, a = 134775813, b = 1")
print("Sampled Distribution Plot for 100 values generated using Linear Congruence Generator : ")
Y_100 = []
x = 0.57
for i in range(100):
     x = (134775813*x + 1)%4294967296
     Y_100.append(x/4294967296)
plt.hist(Y_100, density=True, bins=30,rwidth = 0.8)
plt.title("Sampled Distribution Plot for 100 values generated using Linear Congruence Generator")
plt.show()
print("------------------------------------------------------------------------------------------------------------------")

print("Sampled Distribution Plot of first 100000 values using Vander Corput Sequence : ")
Y_100 = []
for i in range(100000):
    Y_100.append(calc_inverse(i,2))
plt.hist(Y_100,density=True,bins=30,rwidth = 0.8)
plt.title("Distribution Plot for first 100000 values using Vander Corput Sequence")
plt.show()

print("Linear Confruence Generator used : m = 4294967296, a = 134775813, b = 1")
print("Sampled Distribution Plot for 100000 values generated using Linear Congruence Generator : ")
Y_100000 = []
x = 0.57
for i in range(100000):
     x = (134775813*x + 1)%4294967296
     Y_100000.append(x/4294967296)
plt.hist(Y_100000, density=True, bins=30,rwidth = 0.8)
plt.title("Sampled Distribution Plot for 100000 values generated using Linear Congruence Generator")
plt.show()
print("------------------------------------------------------------------------------------------------------------------")
