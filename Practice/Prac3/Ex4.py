def mirror(s):
    res = ""
    for i in range(len(s)):
        k=s[len(s)-i-1]
        if not k in ('b','d','i','o','p','v','w','x'):
            return "NOT POSSIBLE"
        elif k in ('i','o','v','w','x'):
            res+=k
        elif k=='b':
            res+='d'
        elif k=='p':
            res+='q'
        elif k=='q':
            res+='p'
        else:
            res+='b'
    return res
