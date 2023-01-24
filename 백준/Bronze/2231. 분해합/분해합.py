import sys
read= sys.stdin.readline


num = int(read())
count = False
for val in range(1,num):
    sum = val
    val2 = str(val)
    for i in range(len(val2)):
        sum+=int(val2[i])
    if sum==num:
        print(val)
        count=True
        break
if count==False:
    print(0)