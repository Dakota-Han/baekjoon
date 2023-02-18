import sys
from collections import deque
read = sys.stdin.readline



dx = [-2,-2,-1,-1,1,2,2,1]
dy = [-1,1,-2,2,-2,-1,1,2]

def BFS(s1,s2,d1,d2):
    s1= s1+1
    s2=s2+1
    d1=d1+1
    d2=d2+1
    q = deque()
    q.append((s1,s2))
    count = 0
    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a+dx[i]
            ny = b+dy[i]
            if  0<nx<=L and 0<ny<=L and visit[nx][ny]==1:
                visit[nx][ny] = visit[a][b]+1
                q.append((nx,ny))
            if (nx == d1) and (ny == d2):
                ans = (visit[nx][ny]-1)
                return ans
                count = 1
                break
        if count == 1:
            break
            
N = int(read())
res = []
for t in range(N):
    L=int(read())
    a,b = map(int,read().split())
    c,d = map(int,read().split())
    visit = [[1]*(L+1) for _ in range(L+1)]
    if a==c and b==d:
        res.append(0)
    else:
        res.append(BFS(a,b,c,d))

for i in res:
    print(i)