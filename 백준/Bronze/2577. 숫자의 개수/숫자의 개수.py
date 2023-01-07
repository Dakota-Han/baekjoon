import sys
read = sys.stdin.readline

sum = 1
for i in range(3):
    sum*=int(read())

sum2 = str(sum)

for i in range(0,10):
    count=0
    for j in range(len(sum2)):
        if int(sum2[j]) == i:
            count+=1
    print(count)