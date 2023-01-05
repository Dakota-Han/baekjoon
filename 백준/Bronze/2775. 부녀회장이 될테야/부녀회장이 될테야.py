import sys
read = sys.stdin.readline


def floor(k,n):
    res = 0
    if k==0:
        res = n
    elif n==1:
        res = 1
    else:
        res = floor(k,n-1) + floor(k-1,n)
    return res


turn = int(read())

ans = []
for i in range(turn):
    a = int(read())
    b = int(read())
    print(floor(a,b))
