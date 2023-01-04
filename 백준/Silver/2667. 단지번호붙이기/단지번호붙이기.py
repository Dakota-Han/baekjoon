import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
res = []
count = 0
graph = [ list(map(int,read().rstrip())) for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y]=0
    sum = 0
    while q:
        x,y = q.popleft()
        sum+=1
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny>=N:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0
    # for i in range(7):
    #     print(graph[i])
    # print('\n')
    return sum


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            res.append(bfs(i,j))
            count+=1
res.sort()


print(count)
for i in range(len(res)):
    print(res[i])


