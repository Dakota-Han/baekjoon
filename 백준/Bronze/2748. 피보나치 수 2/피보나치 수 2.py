import sys
read = sys.stdin.readline

n = int(read())
g = [0]*91
g[0] = 0
g[1] = 1
g[2] = 1

for i in range(3,91):
    g[i] = g[i-1] + g[i-2]

print(g[n])