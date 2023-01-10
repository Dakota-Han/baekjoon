import sys
read = sys.stdin.readline

val = read().rstrip()
lis  = []

for i in range(len(val)):
    lis.append(val[i])
val=lis
count = 0
if len(val)!=0:
    if val[0]==' ':
        val=val[1:]
    for i in range(len(val)):
        if val[i]==' ':
            count+=1
    print(count+1)
else:
    print('0')
