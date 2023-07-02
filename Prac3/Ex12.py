temp1={'a': 3, 'b': 2, 'c': 1}
temp2={'b': 3, 'c': 2, 'd': 1}
def merge_dict(d1:dict, d2:dict):
    res=dict()
    for i in d1.keys():
        res[i]=d1[i] if i not in d2 else d1[i]+d2[i]
    for i in d2.keys():
        res[i] = d2[i] if i not in d1 else d1[i] + d2[i]

    print(res)
merge_dict(temp1,temp2)

