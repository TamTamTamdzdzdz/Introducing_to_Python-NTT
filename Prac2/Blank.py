
# def dec_to_bin(n):
#     L = []
#     if n == 0:
# 		L.append("0")
# 	elif n == 1:
# 		L.append("1")
# 	else:
# 		a = n%2
# 		L.append(str(a))
# 		dec_to_bin(n//2)
# 	return ''.join(L[::-1])
# print(dec_to_bin(123))
L=[]
def dec_to_bin(n):

    if n==0:
        L.append('0')
    elif n==1:
        L.append('1')
    else:
        a=n%2
        L.append(str(a))
        dec_to_bin(n//2)
    return ''.join(L[::-1])
print(dec_to_bin(120))