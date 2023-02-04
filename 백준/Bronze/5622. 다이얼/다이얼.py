import sys
read = sys.stdin.readline

val = read().rstrip()
val2 = []
sum = 0
for i in range(len(val)):
    temp = val[i]
    if temp in ['A','B','C']:
        sum+=3
    elif temp in ['D','E','F']:
        sum+=4
    elif temp in ['G','H','I']:
        sum+=5
    elif temp in ['J','K','L']:
        sum+=6
    elif temp in ['M','N','O']:
        sum+=7
    elif temp in ['P','Q','R','S']:
        sum+=8
    elif temp in ['T','U','V']:
        sum+=9
    elif temp in ['W','X','Y','Z']:
        sum+=10
    else:
        sum+=11

print(sum)


