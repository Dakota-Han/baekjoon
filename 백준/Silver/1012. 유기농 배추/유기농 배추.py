import sys
from collections import deque
read = sys.stdin.readline


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[b][a]=0

    while q:
        a,b=q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or ny < 0 or nx>=M or ny>=N:
                continue
            if graph[ny][nx] == 1:
                q.append((nx,ny))
                graph[ny][nx] = 0
            
            
turn = int(read())
res = []
for i in range(turn):
    M, N, K = map(int,read().split())

    graph = [[0]*(M) for _ in range(0,N)]   


    for i in range(K):
        a,b = map(int,read().split())
        graph[b][a] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                bfs(i,j)
                count+=1
    res.append(count)

for i in range(len(res)):
    print(res[i])