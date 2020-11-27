import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import statistics

def slot(x):
	size = 20/100
	return int(np.floor((x+10)/size))

def dist(x,me,var):
	return ((math.exp(-0.5*(x-me)*(x-me)/(var*var)))/(var*math.sqrt(math.pi*2)))


## FOR MARSAGLIA-BRAY METHOD
def generate():
	n = 50
	st = time.time()
	ans = []
	mean1 = []
	mean2 = []
	cnt = 0
	for i in range(n):
		u = random.random()
		v = random.random()
		u = 2*u-1
		v = 2*v-1
		cnt=cnt+1
		
		X = u*u+v*v
		if(X<=1):
			Y = math.sqrt(-2*math.log(X)/X)
			z1 = u*Y
			z2 = v*Y
			ans.append(z1) 
			ans.append(z2)         	 # we can write any z = sigma*(z normal) + mean
			mean1.append(z1*math.sqrt(5))   # since the mean = 0 and variance  = 5
			mean1.append(z2*math.sqrt(5))   # since the mean = 0 and variance  = 5
			mean2.append(z1*math.sqrt(5)+5) # since the mean = 5 and variance  = 5
			mean2.append(z2*math.sqrt(5)+5) # since the mean = 5 and variance  = 5
 		
		
				
	time_execution = time.time()-st
	mn = statistics.mean(ans)
	var  = statistics.variance(ans)
	print("Mean generated for 100 values is ",mn)
	print("Variance generated for 100 values is ",var)
	print("Time of execution for 100 values is ", time_execution)
	
	# for N(0,1)
	tot = 100
	size = 20/100
	x = []
	
	i = -10
	
	for j in range(100):
		x.append(i)
		i = i + size
	
	f = [0]*100
	for num in ans:
		if num>=-10 and num < 10:
			f[slot(num)]+=1
			
	length = size*len(ans)
	# scaling the f curve
	for i in range(len(f)):
		f[i]=f[i]/length
		
	plt.plot(x,f)
	plt.show()
	
	# for N(0,5)
	tot = 100
	size = 20/100
	x = []
	
	i = -10
	
	for j in range(100):
		x.append(i)
		i = i + size
	
	f = [0]*100
	for num in mean1:
		if num>=-10 and num < 10:
			f[slot(num)]+=1
			
	length = size*len(mean1)
	# scaling the f curve
	for i in range(len(f)):
		f[i]=f[i]/length
		
	plt.plot(x,f)
	
	z = np.linspace(-10,10,5000,endpoint= True)
	ad = []
	si = 20/5000
	st = -10
	for i in range(5000):
		cur = dist(st,0,math.sqrt(5))
		ad.append(cur)
		st = st+si
	
	plt.plot(z,ad)
	plt.show()
	
	# for N(5,5)
	tot = 100
	size = 20/100
	x = []
	
	i = -10
	for j in range(100):
		x.append(i)
		i = i + size
	
	f = [0]*100
	for num in mean2:
		if num>=-10 and num < 10:
			f[slot(num)]+=1
			
	length = size*len(mean2)
	# scaling the f curve
	for i in range(len(f)):
		f[i]=f[i]/length
		
	plt.plot(x,f)
	z = np.linspace(-10,10,5000,endpoint= True)
	ad = []
	si = 20/5000
	st = -10
	for i in range(5000):
		cur = dist(st,5,math.sqrt(5))
		ad.append(cur)
		st = st+si
	
	plt.plot(z,ad)
	plt.show()
	
	
	print("Proportion of Values Rejected for 100 samples = ", (100-len(ans))/100)
	
generate();

def generate():
	n = 5000
	st = time.time()
	ans = []
	mean1 = []
	mean2 = []
	cnt = 0
	for i in range(n):
		u = random.random()
		v = random.random()
		u = 2*u-1
		v = 2*v-1
		cnt=cnt+1
		
		X = u*u+v*v
		if(X<=1):
			Y = math.sqrt(-2*math.log(X)/X)
			z1 = u*Y
			z2 = v*Y
			ans.append(z1) 
			ans.append(z2)         	 # we can write any z = sigma*(z normal) + mean
			mean1.append(z1*math.sqrt(5))   # since the mean = 0 and variance  = 5
			mean1.append(z2*math.sqrt(5))   # since the mean = 0 and variance  = 5
			mean2.append(z1*math.sqrt(5)+5) # since the mean = 5 and variance  = 5
			mean2.append(z2*math.sqrt(5)+5) # since the mean = 5 and variance  = 5
 		
		
				
	time_execution = time.time()-st
	mn = statistics.mean(ans)
	var  = statistics.variance(ans)
	print("Mean generated for 10000 values is ",mn)
	print("Variance generated for 10000 values is ",var)
	print("The time of execution for 10000 values is ",time_execution)
	
	# for N(0,1)
	tot = 100
	size = 20/100
	x = []
	
	i = -10
	
	for j in range(100):
		x.append(i)
		i = i + size
	
	f = [0]*100
	for num in ans:
		if num>=-10 and num < 10:
			f[slot(num)]+=1
			
	length = size*len(ans)
	# scaling the f curve
	for i in range(len(f)):
		f[i]=f[i]/length
		
	plt.plot(x,f)
	plt.show()
	
	
	# for N(0,5)
	tot = 100
	size = 20/100
	x = []
	
	i = -10
	
	for j in range(100):
		x.append(i)
		i = i + size
	
	f = [0]*100
	for num in mean1:
		if num>=-10 and num < 10:
			f[slot(num)]+=1
			
	length = size*len(mean1)
	# scaling the f curve
	for i in range(len(f)):
		f[i]=f[i]/length
		
	plt.plot(x,f)
	z = np.linspace(-10,10,5000,endpoint= True)
	ad = []
	si = 20/5000
	st = -10
	for i in range(5000):
		cur = dist(st,0,math.sqrt(5))
		ad.append(cur)
		st = st+si
	
	plt.plot(z,ad)
	plt.show()
	
	# for N(5,5)
	tot = 100
	size = 20/100
	x = []
	
	i = -10
	
	for j in range(100):
		x.append(i)
		i = i + size
	
	f = [0]*100
	for num in mean2:
		if num>=-10 and num < 10:
			f[slot(num)]+=1
			
	length = size*len(mean2)
	# scaling the f curve
	for i in range(len(f)):
		f[i]=f[i]/length
		
	plt.plot(x,f)
	z = np.linspace(-10,10,5000,endpoint= True)
	ad = []
	si = 20/5000
	st = -10
	for i in range(5000):
		cur = dist(st,5,math.sqrt(5))
		ad.append(cur)
		st = st+si
	
	plt.plot(z,ad)
	plt.show()
	
	print("Proportion of Values Rejected for 10000 samples = ",(10000-len(ans))/10000)
	

generate();
