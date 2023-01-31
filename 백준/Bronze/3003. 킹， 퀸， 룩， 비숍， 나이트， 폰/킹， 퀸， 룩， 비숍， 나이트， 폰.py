import sys
read = sys.stdin.readline

val = list(map(int,read().split()))

one = [1,1,2,2,2,8]

for i in range(6):
    val[i] = one[i]-val[i]


for i in range(6):
    print(val[i],end=' ')
print()