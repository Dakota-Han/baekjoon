import sys
read = sys.stdin.readline

val = list(map(int,read().split()))
case = 0

if val[0]==val[1]==val[2]:
    sum = val[0]*1000 + 10000

elif (val[0]==val[1] and val[0]!=val[2]):
    sum = 1000+ val[0]*100
elif (val[0]==val[2] and val[0]!=val[1]):
    sum = 1000 + val[0]*100
elif(val[1]==val[2] and val[1]!=val[0]):
    sum = 1000 + val[1]*100
elif (val[0]!=val[1] and val[0]!=val[2] and val[1]!=val[2]):
    sum = max(val)*100

print(sum)


