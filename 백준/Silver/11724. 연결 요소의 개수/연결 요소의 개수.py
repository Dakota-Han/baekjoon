import sys
from collections import deque
read = sys.stdin.readline

N,M = map(int,read().split())
g = [[0]*N for _ in range(N)]
visit  = [0]*N

for i in range(M):
    a,b = map(int,read().split())
    g[a-1][b-1]=g[b-1][a-1]=1

vi = 1

def bfs():

    q=deque()
    global vi
    vi = 1
    for k in range(1,N+1):
        if visit[k-1]==0:
            q.append(k)
            visit[k-1]=vi
            while q:
                v = q.popleft()
                for i in range(N):
                    if g[v-1][i]==1 and visit[i]==0:
                        q.append(i+1)
                        visit[i]=vi
            vi+=1

bfs()
print(vi-1)