import sys
read = sys.stdin.readline

val = list(map(int,read().split()))

val.sort()
print(val[1])
