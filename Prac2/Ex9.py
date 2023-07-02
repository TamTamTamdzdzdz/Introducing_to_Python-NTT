bc=lambda b,c:b if b>c else c

f=lambda a,b,c: a if a>bc(b,c) else bc(b,c)
print(f(4,5,6))