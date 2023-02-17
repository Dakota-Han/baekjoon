import sys
read = sys.stdin.readline


val = read()
now=0
for i in range(0,(len(val)//10)):
    print(val[10*i:10*(i+1)])
    now = 10*(i+1)

print(val[now:])