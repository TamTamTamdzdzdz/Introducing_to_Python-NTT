import time

import Ex5
def Fibo(n):
    count=n-1
    bef=1
    aft=1
    while count>0:
        temp=aft
        aft=aft+bef
        bef=temp
        count-=1
    return bef
print("{0:<10}{1:<20}{2:<30}{3:<40}".format("n","Result","Looping Time","Recursion Time"))
for i in range(30,36):
    Loop_bef=time.time()
    value1=Fibo(i)
    Loop_aft=time.time()
    Rec_bef=time.time()
    value=Ex5.fibo(i)
    Rec_aft=time.time()
    print("{0:<10}{1:<20}{2:<30}{3:<40}".format(i,value,10**10*(Loop_aft-Loop_bef),Rec_aft-Rec_bef))