import time


def GCD(a,b):
    if a%b==0 or b%a==0:
        return min(a,b)
    else:
        return GCD(max(a,b)-min(a,b),min(a,b))

