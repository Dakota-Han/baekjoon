import sys
read = sys.stdin.readline

val = read().rstrip().lower()
alpha = [0]*26


for i in range(len(val)):
    alpha[ord(val[i])-97]+=1

ans=max(alpha)

count = 0
for i in range(26):
    if alpha[i]==ans:
        count+=1
    if count>=2:
        ans = '?'
        break

if ans != '?':
    now = alpha.index(ans)
    ans = chr(now+97).upper()

print(ans)