import sys
read = sys.stdin.readline

val = read().rstrip()
val = list(val)
sum=0
i=0
while len(val)>0:
    if len(val) >=2:
        if val[i]=='c' and val[i+1]=='=':
            del val[:2]
            sum+=1
        elif val[i]=='c' and val[i+1]=='-':
            del val[:2]
            sum+=1
        elif val[i]=='d' and val[i+1]=='-':
            del val[:2]
            sum+=1
        elif val[i]=='l' and val[i+1]=='j':
            del val[:2]
            sum+=1
        elif val[i]=='n' and val[i+1]=='j':
            del val[:2]
            sum+=1
        elif val[i]=='s' and val[i+1]=='=':
            del val[:2]
            sum+=1
        elif val[i]=='z' and val[i+1]=='=':
            del val[:2]
            sum+=1
        elif (len(val)>=3) and val[i] == 'd' and val[i+1]=='z' and val[i+2]=='=':
            del val[:3]
            sum+=1
        else:
            del val[0]
            sum+=1
    

    else:
        del val[0]
        sum+=1
       
print(sum)
