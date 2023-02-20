import sys
read = sys.stdin.readline

N = int(read())
a=[]
for i in range(N):
    a.append(int(read()))

a.sort()

for i in a:
    print(i)