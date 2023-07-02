
def remove_duplicates( l:list[int]):
    res=[]
    if(len(l)<=1):
        return l
    res.append(l[0])
    for i in range (len(l)-1):
        if(l[i]!=l[i+1]):
            res.append(l[i+1])
    return res

