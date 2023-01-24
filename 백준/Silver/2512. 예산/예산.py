import sys
read = sys.stdin.readline
n = int(read())
val = list(map(int,read().split()))
total = int(read())

end = max(val)
start = 1
mid = (end+start)//2
res = []
while start<=end:
    mid = (end+start)//2
    sum=0
    for i in range(len(val)):
        if val[i] > mid:
            sum = mid + sum
        else:
            sum = val[i] + sum
    if sum > total:
        end = mid -1
    elif sum <= total:
        start = mid + 1
        res.append(mid)

print(max(res))