import sys
read = sys.stdin.readline
N = int(read())

s = 666
i=0
while True:
    if '666' in str(s):
        i+=1
    s+=1
    if i == N:
        break

print(s-1)

