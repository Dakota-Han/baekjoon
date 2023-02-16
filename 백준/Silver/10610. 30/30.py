import sys
read = sys.stdin.readline

n = list(read().rstrip())
n.sort(reverse=True)

sum=0
for i in n:
    sum+=int(i)
if sum%3!=0 or ('0' not in n):
    print(-1)
else:
    str1=''
    for i in n:
        str1+=i
    print(str1) 
