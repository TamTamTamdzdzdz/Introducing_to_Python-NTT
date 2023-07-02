def combination(n,k):
    res=1
    for i in range (1,k+1):
        res=res*(n-i+1)/i
    return res
def pascal_triangle1(n):
    res=''
    for i in range(n):
        res+=str(int(combination(n,i)))+' '
    res+=str(1)
    return res



def display_pascal_triangle(n):
    length=len(pascal_triangle1(n))
    for i in range(n):
        temp=' '*(n-i-1)+pascal_triangle1(i)+' '*(n-i-1)
        print(temp)


