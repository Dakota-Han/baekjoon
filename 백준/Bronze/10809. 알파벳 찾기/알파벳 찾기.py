import sys

read=sys.stdin.readline
val = read().rstrip()
list=[-1]*26
for i in range(97,123):
    if chr(i) in val:
        list[i-97]=val.index(chr(i))
        continue
     
for i in range(26):
    print(list[i],end=' ')
    
print()

