from functools import reduce

s = input()
temp=s.split('_')
temp=map(lambda  x:str(x).capitalize(),temp)
res= reduce(lambda x,y:x+y,temp)
print(res)