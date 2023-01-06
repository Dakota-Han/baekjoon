import sys
read = sys.stdin.readline

val = []
for i in range(9):
    val.append(int(read()))

print(max(val))
print(val.index(max(val))+1)
