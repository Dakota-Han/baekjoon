import sys
read = sys.stdin.readline

N = read()

if int(N)<10:
    N = '0'+N


def new(val):
    a = val[0]
    b = val[1]
    c = str(int(a)+int(b))
    return b+c[-1]

now = N
count = 0
while True:
    now = new(now)
    count+=1
    if int(now) == int(N):
        break
print(count)

