import sys
read= sys.stdin.readline


num = int(read())
res=[]
for i in range(num):
    val=read().rstrip()
    count = 0
    ans = 0
    sum=0
    for i in range(len(val)):
        if val[i] == 'O':
            count=count+1
            sum = count+sum
        if val[i]=='X':
            ans+=sum
            count=0
            sum=0
        if i == len(val)-1:
            ans+=sum

    res.append(ans)


for i in range(num):
    print(res[i])
        
