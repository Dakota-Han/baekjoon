import sys
read = sys.stdin.readline

val = []
for i in range(1,92):
    a=[0]*2
    val.append(a)

val[1][1]=1
val[2][0]=1
val[3][0]=1
val[3][1]=1
for i in range(4,91):
    val[i][0] = val[i-1][0] + val[i-1][1]
    val[i][1] = val[i-1][0]

num = int(read())
print(val[num][0]+val[num][1])
