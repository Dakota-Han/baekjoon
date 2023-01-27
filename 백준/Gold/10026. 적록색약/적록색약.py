import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
g = []
v = [[0]*N for _ in range(N)]

for  i in range(N):
    a = []
    temp = read().rstrip()
    for i in range(N):
        a.append(temp[i])
    g.append(a)
sum = 0
def bfs(a,b,color):
    dx= [-1,1,0,0]
    dy = [0,0,-1,1]
    q=deque()
    q.append((a,b))
    v[a][b] = 1 
    while q:
        c,d = q.popleft()
        for i in range(4):
            nx = c+dx[i]
            ny = d+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if v[nx][ny] == 0 and g[nx][ny] == color:
                q.append((nx,ny))
                v[nx][ny]=1


def bfs2(a,b):
    dx= [-1,1,0,0]
    dy = [0,0,-1,1]
    q=deque()
    q.append((a,b))
    v[a][b] = 1 
    while q:
        c,d = q.popleft()
        for i in range(4):
            nx = c+dx[i]
            ny = d+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if v[nx][ny] == 0 and (g[nx][ny] == "R" or g[nx][ny]=='G'):
                q.append((nx,ny))
                v[nx][ny]=1

colors = ['R','G','B']

for color in colors:
    for i in range(N):
        for j in range(N):
            if v[i][j]==0 and g[i][j]==color:
                bfs(i,j,color)
                sum+=1
sum2 = 0

v = [[0]*N for _ in range(N)]

for i in range(N):
        for j in range(N):
            if v[i][j]==0 and g[i][j]=='B':
                bfs(i,j,'B')
                sum2+=1
for i in range(N):
    for j in range(N):
        if v[i][j]==0:
            bfs2(i,j)
            sum2+=1


print(sum)
print(sum2)
        
