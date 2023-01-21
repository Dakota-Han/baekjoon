import sys
read = sys.stdin.readline

N,C = map(int,read().split())
val = []
for i in range(N):
    a = int(read().rstrip())
    val.append(a)
val.sort()

end = val[-1]-val[0]
start=1
result = 0


while start<=end:
    mid = (start+end)//2
    now = val[0]
    count = 1
    for i in range(1,N):
        if val[i] >= now + mid:
            count+=1
            now = val[i]
    if count >= C:
        start = mid+1
        result = mid
    elif count < C:
        end = mid-1
    

print(result)