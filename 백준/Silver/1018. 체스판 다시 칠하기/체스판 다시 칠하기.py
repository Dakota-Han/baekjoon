import sys
read = sys.stdin.readline

N,M = map(int,read().split())
val = []
for _ in range(N):
    a=[]
    temp = read()
    for i in range(M):
        a.append(temp[i])
    val.append(a)

def find(val):
    res1=0
    res2=0
    for i in range(8):
        for j in range(8):
            if(i%2==0) and(j%2==0):
                if val[i][j]!='W':
                    res1+=1
            elif(i%2==1) and(j%2==1):
                if val[i][j]!='W':
                    res1+=1
            else:
                if val[i][j]!='B':
                    res1+=1
        
    for i in range(8):
        for j in range(8):
            if(i%2==0) and(j%2==0):
                if val[i][j]!='B':
                    res2+=1
            elif(i%2==1) and(j%2==1):
                if val[i][j]!='B':
                    res2+=1
            else:
                if val[i][j]!='W':
                    res2+=1
    return(min(res2,res1))


ans = []
for i in range(N-7):
    temp = val[i:i+8]
    for j in range(M-7):
        temp2=[]
        for k in temp:
            temp2.append(k[j:j+8])
        ans.append(find(temp2))
        # find(val[i:i+9][j:j+9])

print(min(ans))