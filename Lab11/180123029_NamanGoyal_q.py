import numpy as np
import time
import statistics
import math
import random
import matplotlib.pyplot as plt

print("")

# for N = 10
print("Number of sub-intervals of [0,1] of equal lengths : 10")
x = 0.42
m = 4294967296
a = 134775813
b = 1
freq_arr = [0]*10
for i in range(10000):
    x = (a*x + b)%m
    freq_arr[math.floor(10 * x/m)] += 1  
ans = 0
for i in range(10):
    ans = max(ans,abs(freq_arr[i]/10000 - 1/10))
print("The value of discrepancy when N = 10 is",ans)
print("")

# for N = 20
print("Number of sub-intervals of [0,1] of equal lengths : 20")
x = 0.42
m = 4294967296
a = 134775813
b = 1
freq_arr = [0]*20
for i in range(10000):
    x = (a*x + b)%m
    freq_arr[math.floor(20 * x/m)] += 1  
ans = 0
for i in range(20):
    ans = max(ans,abs(freq_arr[i]/10000 - 1/20))
print("The value of discrepancy when N = 20 is",ans)
print("")

# for N = 50
print("Number of sub-intervals of [0,1] of equal lengths : 50")
x = 0.42
m = 4294967296
a = 134775813
b = 1
freq_arr = [0]*50
for i in range(10000):
    x = (a*x + b)%m
    freq_arr[math.floor(50 * x/m)] += 1  
ans = 0
for i in range(50):
    ans = max(ans,abs(freq_arr[i]/10000 - 1/50))
print("The value of discrepancy when N = 50 is",ans)
print("")

# for N = 100
print("Number of sub-intervals of [0,1] of equal lengths : 100")
x = 0.42
m = 4294967296
a = 134775813
b = 1
freq_arr = [0]*100
for i in range(10000):
    x = (a*x + b)%m
    freq_arr[math.floor(100 * x/m)] += 1  
ans = 0
for i in range(100):
    ans = max(ans,abs(freq_arr[i]/10000 - 1/100))
print("The value of discrepancy when N = 100 is",ans)
