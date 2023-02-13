import sys
from collections import deque
read = sys.stdin.readline
N = int(read())

g=[]
for i in range(N):
    a = list(map(int,read().split()))
    g.append(a)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans = [0]

def bfs(a,b,k):
    q = deque()
    q.append((a,b))
    visit[a][b]=1
    while q:
        c,d = q.popleft()
        for i in range(4):
            nx = dx[i] + c
            ny = dy[i] + d
            if 0<=nx<N and 0<=ny<N and g[nx][ny]>k and visit[nx][ny]==0:
                visit[nx][ny] =1
                q.append((nx,ny))



k=0
while True:
    visit = [[0]*N for _ in range(N)]
    count = 0    
    for i in range(N):
        for j in range(N):
            if g[i][j] > k and visit[i][j]==0:
                bfs(i,j,k)
                count+=1
    if count == 0 :
        break
    ans.append(count)
    k+=1
print(max(ans))
