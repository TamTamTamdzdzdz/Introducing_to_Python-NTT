from collections import Counter
import re


with open('test.inp','r') as f:
    # mystring=f.read()
    lines=list()
    for line in f:
        lines.append(line)
    mystring=''.join(lines)
    res=mystring.replace('\n','\n ')

with open('test.out','w') as output:
    temp=re.split(r'[ \t]+', res)
    output.write(str(dict(Counter(temp))))
with open('test.out','r') as f:
    all=f.read()
    print(all)
f.close()






# from collections import Counter
#
# # Read the contents of test.inp
# with open('test.inp', 'r') as f:
#     lines = f.readlines()
#
# # Count the frequency of each word
# word_count = Counter()
# for line in lines:
#     word_count.update(line.split())
# print(word_count)
# # Write the resulting dictionary to test.out
# with open('test.out', 'w') as f:
#     f.write(str(dict(word_count)))