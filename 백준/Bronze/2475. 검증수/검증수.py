import sys
read=sys.stdin.readline

val = list(map(int,read().split()))
sum=0
for i in val:
    now = i*i
    sum+=now
print(sum%10)