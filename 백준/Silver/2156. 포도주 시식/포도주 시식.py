import sys
read = sys.stdin.readline

n = int(read())
val=[]



for i in range(n):
    a = int(read())
    val.append(a)

sum_1=[0]*n
sum_2=[0]*n
sum_1[0]=val[0]
sum_2[0]=val[0]
if n>=2:
    sum_1[1]=val[1]+val[0]
    sum_2[1]=val[1]
    if n>=3:
        sum_2[2]=val[2]+val[0]
        sum_1[2]=val[2]+val[1]
        for i in range(3,n):
            sum_1[i] = val[i]+val[i-1]+max(max(sum_1[0:i-2]),max(sum_2[0:i-2]))
            sum_2[i] = val[i]+max(max(sum_1[0:i-1]),max(sum_2[0:i-1]))

max1 = max(sum_1)
max2 = max(sum_2)
print(max(max1,max2))

