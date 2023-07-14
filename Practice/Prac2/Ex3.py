def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,n,1):
        if n%i==0:
            return False
    return True
def print_prime(n):
    for i in range(1,n):
        if(is_prime(i)):
            print(i,end=' ')
