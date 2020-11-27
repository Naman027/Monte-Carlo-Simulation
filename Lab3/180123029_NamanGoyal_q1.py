import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


odd_val=[]
for i in range(10000):
    if i%2==1:
        odd_val.append(i)

cur=0

any_value=np.random.uniform(0,1,100000)
ans=[]
ans.append(0)
#firstly inserting the values onto the ans array
for i in range(5000):
    cur=cur+1
    ans.append(cur/5000)
print_ans=[]
for v in any_value:
    for j in range(5000):
        if v>ans[j] and v<=ans[j+1]:
            print_ans.append(odd_val[j])
            break
            
            
print(print_ans)

