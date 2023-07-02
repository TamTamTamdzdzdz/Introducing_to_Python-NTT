def dictionary_convert(s):
    count=dict()
    for char in s:
        count[char]=count.get(char,0)+1
    print(count)
