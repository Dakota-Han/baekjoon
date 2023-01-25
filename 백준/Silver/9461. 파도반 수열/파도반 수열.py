import sys
read = sys.stdin.readline
T = int(read())
num = []
for i in range(T):
    a = int(read())
    num.append(a)


res=[]
for N in num:
    val = [1,1,1,2,2]
    if N>=5:
        val2 = [0]*(N-5)
        val = val+val2
       
        for i in  range(5,N):
            val[i]=val[i-1]+val[i-5]
    res.append(val[N-1])

for i in res:
    print(i)