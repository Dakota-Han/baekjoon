import sys
from collections import deque
read = sys.stdin.readline

M,N = map(int,read().split())

graph = [ list(map(int,read().split())) for i in range (N)]
start = []
ans =[]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            start.append((i,j))


def bfs(a,b):
    res = []
    q = deque()
    q.append((a,b))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = dx[i] + b
            ny = dy[i] + a
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if graph[ny][nx] != 1 and graph[ny][nx] !=-1:
                graph[ny][nx] = 1
                res.append((ny,nx))
    return res

count = 0
ans = start


while True:
    temp =[]
    for i in range(len(ans)):
        a,b=ans[i]
        temp+=bfs(a,b)
    ans = temp

    if len(temp) == 0:
        break
    count +=1





for i in range(N):
    if 0 in graph[i]:
        count = -1
        break

print(count)

    



