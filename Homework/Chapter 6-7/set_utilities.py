def set_union(A,B):
    res = set()
    for i in A:
        if i not in res:
            res.add(i)
    for i in B:
        if i not in res:
            res.add(i)
    return res
def set_intersection(A,B):
    res = set()
    for i in A:
        if i in B and i not in res:
            res.add(i)
    return res

