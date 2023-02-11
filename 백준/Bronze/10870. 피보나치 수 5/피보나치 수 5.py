import sys
read = sys.stdin.readline

n = int(read())
dp = [0]*21
dp[0]=0
dp[1]=1
dp[2]=1
for i in range(3,21):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])

