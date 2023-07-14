l=[('John', 9.75), ('Max', 9.5), ('James', 9.5), ('Henry', 8.5)]
def sort_students(l):
    l.sort()
    res=[]
    for (v,k) in l:
        res.append((k,v))
    res.sort()
    l.clear()
    for (v,k) in res:
        l.append((k, v))
    return l
