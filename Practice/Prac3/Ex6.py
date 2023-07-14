temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

a = []
b = []
for i in range(m):
  a.append(input().split(' '))
for i in range(m):
  b.append(input().split(' '))
res=[]
for i in range (m):
    tmp=[]
    for j in range (n):

        tmp.append(int(a[i][j])+int(b[i][j]))
    res.append(tmp)
for i in range (m):
    for j in range(n):
        print(res[i][j],end=' ')
    print(' ')