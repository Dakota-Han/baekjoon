import sys
read = sys.stdin.readline

N = int(read())
val = []
for i in range(N):
    now = read().rstrip()
    length = len(now)
    val.append((length,now))


for i in range(1,51):
    temp = []
    for j in range(1,len(val)+1):
        a,b = val[j-1]
        if a == i:
            temp.append(b)
    temp = set(temp)
    temp = list(temp)
    temp.sort()
    for k in range(len(temp)):
        print(temp[k])
