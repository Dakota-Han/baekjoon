import sys
read = sys.stdin.readline
val = []

N = int(read())
for i in range(N):
    a,b = map(int,read().split())
    val.append((a,b))
res = [0]*N

for i in range(N):
    count=1
    for j in range(N):
        na,nb = val[i]
        a,b = val[j]
        if (a>na and b>nb):
            count+=1
        res[i] = count
for i in res:
    print(i,end=' ')
print()