import sys
read = sys.stdin.readline

N = int(read().rstrip())

sum = 0
i = 1
count = 0

while True:
    if (N-sum>=i):
        sum+=i
        count+=1
    
    else:
        break
    i+=1

if N==1:
    print(1)
else:
    print(count)

