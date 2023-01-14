import sys
read = sys.stdin.readline

turn = int(read())
g = []
for i in range (turn):
    temp=[]
    temp = list(map(int,read().rstrip().split()))
    g.append(temp)


if turn == 1:
    print(g[0][0])
else:
    g[1][0] = g[1][0] + g[0][0]
    g[1][1] = g[1][1] + g[0][0]

    for i in range(2,turn):
        for j in range(i+1):
            if (j-1>=0 and j!=i):
                g[i][j] = max(g[i][j] + g[i-1][j],g[i][j] +g[i-1][j-1])
            elif (i==j):
                g[i][j] = g[i][j] + g[i-1][j-1]
            else:
                g[i][j] = g[i][j] + g[i-1][j]

            
    print(max(g[turn-1]))

