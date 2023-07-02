tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])
for i in range (m):
    start=i*n
    for j in range(n):
        print(start+j+1,end=' ')
    print(' ')
