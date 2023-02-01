import sys
from collections import deque
read = sys.stdin.readline



def bfs(a,b):
    q = deque()
    q.append((a,b))
    visit[a][b] = 1
    g[a][b] = 0

    dx = [-1,1,0,0,-1,1,-1,1]
    dy = [0,0,-1,1,1,-1,-1,1]
    while q:
        c,d = q.popleft()
        for i in range(8):
            nx = c+dx[i]
            ny = d+dy[i]
            if nx<0 or nx>= H or ny<0 or ny>=W or visit[nx][ny]==1:
                continue
            if g[nx][ny]==1:
                q.append((nx,ny))
                visit[nx][ny] = 1
                g[nx][ny]=0

res = []
while True:
    
    count = 0
    W,H = map(int,read().split())
    g = []
    if W==0 and H==0:
        break
    for i in range(H):
        a = list(map(int,read().split()))
        g.append(a)

    visit = [ [0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if g[i][j] == 1:
                bfs(i,j)
                count+=1

    res.append(count)


for i in res:
    print(i)



        

