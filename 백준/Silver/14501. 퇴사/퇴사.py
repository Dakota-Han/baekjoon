import sys
read = sys.stdin.readline

N = int(read())
T = []
P = []
for i in range(N):
    a,b = map(int,read().split())
    T.append(a)
    P.append(b)
T.append(0)
P.append(0)
now = [0]*(N+1)

for i in range(N-1,-1,-1):
    if i+T[i] >N:
        now[i] = now[i+1]
    else:
        now[i] = max(now[i+1],P[i]+now[i+T[i]])

print(now[0])
    
