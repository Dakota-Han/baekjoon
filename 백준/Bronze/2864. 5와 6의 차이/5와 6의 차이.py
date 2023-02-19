import sys
import copy
read=  sys.stdin.readline

a,b =map(int,read().split())
a=str(a)
b=str(b)
a1=[]
b1=[]
for i in range(len(a)):
    a1.append(a[i])

for i in range(len(b)):
    b1.append(b[i])

max_a=copy.deepcopy(a1)
max_b=copy.deepcopy(b1)
min_a=copy.deepcopy(a1)
min_b=copy.deepcopy(b1)

for i in range(len(a1)):
    if a1[i]=='5':
        max_a[i]='6'
    if a1[i]=='6' :
        min_a[i]='5'

for i in range(len(b1)):
    if b1[i] == '5':
        max_b[i]='6'
    if b1[i]=='6':
        min_b[i]='5'
        

ma = ''.join(max_a)
mb = ''.join(max_b)
ma2 = ''.join(min_a)
mb2 = ''.join(min_b)

print(int(ma2)+int(mb2),int(ma)+int(mb))

        