import sys
read = sys.stdin.readline

turn = int(read())
N=30
M=30
graph = [[0]*(31) for _ in range(31)]

for i in range(M+1):
    graph[i][i] = 1

# for i in range(M+1):
#     print(graph[i])
for i in range(1,M+1):
    graph[1][i] = i


for j in range(1,M):
    for i in range(2,M-j+1):
        a=i+j

        graph[i][a] = graph[i-1][a-1]+graph[i][a-1]

res=[]
for i in range(turn):
    N,M = map(int,read().split())
    res.append(graph[N][M])

for i in res:
    print(i)
