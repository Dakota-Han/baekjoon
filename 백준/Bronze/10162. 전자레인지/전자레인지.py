import sys
read = sys.stdin.readline

val = int(read())
min5=min1=minsec=0


if val>=300:
    min5 = val//300
    val = val%300

if val>=60:
    min1 = val//60
    val = val%60


if val >=10:
    minsec = val//10
    val = val%10


if val == 0:
    print(min5, min1, minsec)  

if val != 0:
    print("-1")