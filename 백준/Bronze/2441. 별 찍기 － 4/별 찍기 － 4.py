N = int(input())
for i in range(N,0,-1):
    a = '*'*i
    b = ' '*(N-i)
    print(b+a)