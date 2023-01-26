import sys
read = sys.stdin.readline

N = int(read())
val=[]
for i in range(N):
    a = read().rstrip()
    val.append(a)
sum = 0
for i in val:
    alpha  = []
    word = True
    for j in range(len(i)):
        if (i[j] in alpha) and (alpha[-1]!= i[j]):  
            word = False
            break
        else:
            alpha.append(i[j])
    if word == True:
        sum+=1
print(sum)
    

