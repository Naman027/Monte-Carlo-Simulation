
import numpy as np
import math
import statistics
import random
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SBIN.NS.csv") # define the path of .csv file here
s = df["Adj Close"]
s = s.tolist()

stock_price = [0, 0, 0]
for k in range(1000):
    arr = []
    n = len(s)
    for i in range(1, n):
        cur = math.log(s[i]/s[i-1])
        arr.append(cur)
    mean_arr = sum(arr)/len(arr)

    sum_squares = 0
    for i in range(len(arr)):
        sum_squares += (arr[i]-mean_arr)**2
    variance = sum_squares/(n-1)

    S0 = s[65]
    for i in range(1, 22):
        # np.random.normal generates a normal variable value
        cur_stock = S0*np.exp(mean_arr + math.sqrt(variance)* np.random.normal(0, 1))
        S0 = cur_stock
        if(i==7):
            stock_price[0] += cur_stock
        elif(i==14):
            stock_price[1] += cur_stock
        elif(i==21):
            stock_price[2] += cur_stock
            
# calculating the expected stock price and error in the actual and expected price           
stock_price[0] = stock_price[0]/1000
e1 = (190.70-stock_price[0])/190.70*100
stock_price[1] = stock_price[1]/1000
e2 = (200.05-stock_price[1])/200.05*100
stock_price[2] = stock_price[2]/1000
e3 = (203.75-stock_price[2])/203.75*100

data = [["7th October", 190.70, stock_price[0], e1], ["14th October",
                                                             200.05, stock_price[1], e2], ["21st October", 203.75, stock_price[2], e3]]
df1 = pd.DataFrame(data, columns = ["Date", "Actual Price", "Expected Price", "Percentage Error"])
df1
