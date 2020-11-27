def finding_LCG(a,b,m):
    print('a b m \t\tLCGsequence',end='\n')
    print(a,b,m) 
    for x in range(0,11):
        print('x :',x,'->', end='\t')
        start=x
        for i in range(0,m+1):
            print((start),end=', ')
            current_val=start
            start=(current_val*a+b)%m
            if(start==x):
                print(x,',...'),
                break
                
         
finding_LCG(3,0,11)
print('\n')
finding_LCG(6,0,11)

