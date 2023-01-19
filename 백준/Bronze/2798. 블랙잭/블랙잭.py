import sys
read = sys.stdin.readline

N,M = map(int,read().split())
val = list(map(int,read().split()))
max = 0
for i in range(len(val)):
    for j in range(i+1,len(val)):
        for t in range(j+1,len(val)):
            sum = val[i]+val[j]+val[t]
            if max<sum and sum<=M:
                max = sum

print(max)
