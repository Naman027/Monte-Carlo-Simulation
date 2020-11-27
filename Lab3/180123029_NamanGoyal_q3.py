import matplotlib.pyplot as plt
import numpy as np
from random import randint as rdi
from random import random as rand
c = 1.4 # c>=1.2
prob_arr = [0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]
index = [1,2,3,4,5,6,7,8,9,10]

def fun(arg):
    count = 0 
    while 1:
        count += 1
        x = rdi(1, 10)  
        u = rand()        
        if u*arg*0.1 <= prob_arr[x-1] :
            return x, count

new_arr = [fun(c) for _ in range(1000000)]
new_arr = np.array(list(map(lambda x: x[0], new_arr)))

count_parr = [0]*10
# counting for each value in index array
for ind in index:
    count_parr[ind-1] = np.count_nonzero(new_arr==ind)
count_parr = np.array(count_parr)/1000000
    
plt.bar(index, count_parr)
plt.xlabel('Possible values of t')
plt.ylabel('Probability at X=t')
plt.show()
