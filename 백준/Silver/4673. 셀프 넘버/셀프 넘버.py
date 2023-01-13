
s_num=0
res=[0]*13000
i= 0
temp=0
s_num = 0
while True:
    temp = 0
    for j in range(len(str(i))):
        temp+=int(str(i)[j])
    s_num = temp+i
    if s_num >=13000:
        break
    res[s_num]=1
    i+=1

for i in range(10000):
    if res[i]==0:
        print(i)


