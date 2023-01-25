import sys
read = sys.stdin.readline

num = int(read())
val = list(map(int,read().split()))

sum =[0]*num
sum[0] = val[0]
for i in range(1,len(val)):
    sum[i]=max(val[i],sum[i-1]+val[i])

print(max(sum))
