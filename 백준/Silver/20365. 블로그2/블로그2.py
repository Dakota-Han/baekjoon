import sys
read = sys.stdin.readline

N = int(read())
val = read().rstrip()
val2 = list(val)
val3=[]

count = 0
count2 = 0

val3.append(val2[0])
for i in range(1,N):
    if val[i]!=val[i-1]:
        val3.append(val[i])

for i in range(len(val3)):
    if val3[i]=='B':
        count+=1
    else:
        count2+=1

print(min(count,count2)+1)