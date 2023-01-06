import sys
read = sys.stdin.readline

num = int(read())
val = list(map(int,read().rstrip().split()))

print(min(val),max(val))