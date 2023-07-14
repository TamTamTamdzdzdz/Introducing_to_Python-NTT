
gcd=lambda a,b: min(a,b)if max(a,b)%min(a,b)==0 else gcd (max(a,b)-min(a,b),min(a,b))
print(gcd(10,20))