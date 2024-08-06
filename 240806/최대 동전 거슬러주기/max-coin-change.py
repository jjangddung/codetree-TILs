import sys


n,m = map(int,  input().split())

coin = list(map(int , input().split()))

INT_MIN = -sys.maxsize

dp = [INT_MIN] * (m+1)

dp[0] = 0


for i in range(1,m+1) :
    for  j in range(n) :
        if coin[j] <= i :
            if dp[i-coin[j]] == INT_MIN :
                continue

            dp[i] = max(dp[i], dp[i-coin[j]]+1 )

ans = dp[m]

if ans > 0  :
    print(ans)
else :
    print(-1)