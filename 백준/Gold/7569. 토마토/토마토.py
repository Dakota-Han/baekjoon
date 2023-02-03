import sys
from collections import deque
read = sys.stdin.readline

N,M,H = map(int,read().split())
graph=[[[] for _ in range(M)] for _ in range(H)]
val=[]
for i in range(H):
    for j in range(M):
        graph[i][j] = list(map(int,read().split()))
        for t in range(N):
            if(graph[i][j][t]==1):
                val.append((i,j,t))


def bfs(a,b,c):
    q=deque()
    q.append((a,b,c))

    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    while q:
        # print(q)
        a1,b1,c1 = q.popleft()
        for i in range(6):
            nx = a1 + dx[i]
            ny = b1 + dy[i]
            nz = c1 + dz[i]
            if (0<= nx <H) and (0<= ny <M) and (0<= nz <N):
                if graph[nx][ny][nz]==0 or graph[a1][b1][c1] + 1 < graph[nx][ny][nz]:
                    q.append((nx,ny,nz))
                    graph[nx][ny][nz] = graph[a1][b1][c1] + 1
            
for i in val:
    a,b,c = i
    bfs(a,b,c)

ans = 1
for i in range(H):
    for j in range(M):
        # print(graph[i][j])
        ans = max(ans,max(graph[i][j]))
        if 0 in graph[i][j]:
            print(-1)
            sys.exit(0)

print(ans-1)



