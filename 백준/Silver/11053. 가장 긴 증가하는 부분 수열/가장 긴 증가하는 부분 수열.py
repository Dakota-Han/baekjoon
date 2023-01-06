import sys
read = sys.stdin.readline
num = int(read())
val = list(map(int,read().strip().split()))

store = [1]*(num)

for i in range(num):
    for j in range(i):
        if val[i] > val[j]:
            store[i] = max(store[i],store[j]+1)
    

print(max(store))