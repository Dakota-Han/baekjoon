import sys
from collections import deque

read = sys.stdin.readline

c = int(read())
v = int(read())

graph = [ [0]*(c+1) for _ in range(c+1)]
visit = [0]*(c+1)

for i in range(v):
    a,b = map(int,read().split())
    graph[a][b]=graph[b][a] = 1


def bfs(v):
    count = 0
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        v = q.popleft()
        for i in range(1,c+1):
            if graph[v][i]==1 and visit[i] == 0:
                q.append(i)
                visit[i] = 1
                count += 1
    return count
            

print(bfs(1))
