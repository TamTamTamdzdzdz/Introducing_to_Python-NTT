def dec_to_bin(n):
    res=""
    if(n==0):
        return "0"
    if(n==1):
        return "1"
    else:
        return dec_to_bin(n//2)+(n%2).__str__()
