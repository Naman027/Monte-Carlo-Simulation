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
        k, p = divmod(k, b)
        po *= b
        ans += p/po
    return ans
    
print("------------------------------------------------------------------------------------------------------------------")
print("Halton Sequence with base 2 and base 3")
print("------------------------------------------------------------------------------------------------------------------")
print("Calculating for 100 values")
X_100 = []
Y_100 = []
for i in range(100):
    X_100.append(calc_inverse(i,2))
    Y_100.append(calc_inverse(i,3))

plt.scatter(X_100,Y_100)
plt.axis([0, 1, 0, 1])
plt.show()
print("------------------------------------------------------------------------------------------------------------------")
print("Calculating for 100000 values")
X_100000 = []
Y_100000 = []
for i in range(10000):
    X_100000.append(calc_inverse(i,2))
    Y_100000.append(calc_inverse(i,3))
plt.scatter(X_100000,Y_100000)
plt.axis([0, 1, 0, 1])
plt.show()
print("------------------------------------------------------------------------------------------------------------------")
