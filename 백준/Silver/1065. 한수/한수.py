import sys
read= sys.stdin.readline

val = 12
val = str(val)
temp = int(val[1])-int(val[0])
count=1
sum = 0 
num = read().rstrip()



for val in range(1,int(num)+1):
    if len(str(val)) == 1:

        sum+=1
        continue
    else:
        count = True
        val = str(val)
        temp = int(val[1])-int(val[0])

        for i in range(0,len(val)-1):
            if temp != int(val[i+1])-int(val[i]):
                count = False

                break
        if count == True:

            sum+=1
print(sum)


