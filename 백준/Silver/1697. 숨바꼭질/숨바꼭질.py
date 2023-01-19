import sys
from collections import deque
read = sys.stdin.readline
N,K = map(int,read().split())
visit = [0]*100001

def bfs(N,K):
    q = deque()
    q.append(N)
    visit[N]=1
    while q:
        v = q.popleft()
        if v == K:
            return visit[v]
        for i in [v-1,v+1,v*2]:
            if 0 <= i <= 100000 and visit[i]==0:
                visit[i] = visit[v]+1
                q.append(i)

print(bfs(N,K)-1)
            


