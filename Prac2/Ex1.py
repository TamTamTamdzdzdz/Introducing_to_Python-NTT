def is_perfect(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    return sum==2*n
