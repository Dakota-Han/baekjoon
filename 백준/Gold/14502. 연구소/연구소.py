import sys
from collections import deque
import copy

read = sys.stdin.readline

N,M = map(int,read().split())

g = [ list(map(int,read().split())) for _ in range(N)]

ans = 0

   
def bfs():
    temp=copy.deepcopy(g)
    q = deque()
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i,j))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            
            if (nx<0) or (nx>=N) or (ny<0) or (ny>=M):
                continue
            if temp[nx][ny] != 0:
                continue
            q.append((nx,ny))
            temp[nx][ny]=2
    global ans
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                count+=1
    ans = max(ans,count)
    

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                g[i][j] = 1
                wall(cnt+1)
                g[i][j] = 0
    
wall(0)
print(ans)

