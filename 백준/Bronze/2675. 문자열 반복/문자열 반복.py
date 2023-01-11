import sys
read = sys.stdin.readline

num = int(read())
res= [] 
for k in range(num):
    turn, val = read().rstrip().split()

    pr = ''
    for i in range(len(val)):
        for j in range(int(turn)):
            pr+=val[i]
    
    res.append(pr)
    pr=''


for i in range(len(res)):
    print(res[i])