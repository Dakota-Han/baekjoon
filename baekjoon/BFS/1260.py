import sys
from collections import deque
read = sys.stdin.readline

N, M, V = map(int,read().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
visit2 = [0]*(N+1)

for i in range(M):
    a,b = map(int,read().split())
    graph[a][b]=1
    graph[b][a]=1


def DFS(V):
    q = deque()
    q.append(V)
    while q:
        v = q.popleft()
        visit2[v] = 1
        print(v,end=' ')
        for i in range(1,N+1):
            if visit2[i] == 0 and graph[v][i] == 1:
                DFS(i)
                
        

def BFS(V):
    q = deque()
    q.append(V)
    visit[V] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,N+1):
            if visit[i]==0 and graph[v][i]==1:
                q.append(i)
                visit[i]=1

DFS(V)
print()
BFS(V)
print()

