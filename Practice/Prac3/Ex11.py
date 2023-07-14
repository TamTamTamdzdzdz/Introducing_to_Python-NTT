n = int(input())
s = input()
res=""
for i in s:
    k= ord(i)+n%26
    if i==' ':
        res+=' '
    elif k<=122:
        res+=chr(k)
    else:
        res+=chr(k-26)
print(res)