import sys
read= sys.stdin.readline

val = int(read())
sum = 1
if val !=0:
    for i in range(1,val+1,1):
        sum=sum*i
    print(sum)
else:
    print(1)

