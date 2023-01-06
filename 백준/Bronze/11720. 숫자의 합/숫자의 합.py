import sys
read = sys.stdin.readline

num = int(read())
num2 = read()

sum = 0
for i in range(num):
    sum = int(num2[i])+sum

print(sum)
