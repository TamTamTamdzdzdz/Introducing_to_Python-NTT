def transform(l):

    return list(map(lambda x:2*x if x%2==0 else x*-1,l))
l=[32, 56, 99, -40, 20, 78, 43, -61, 61]
print(transform(l))