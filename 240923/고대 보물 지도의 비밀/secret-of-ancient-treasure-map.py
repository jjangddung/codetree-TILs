import sys


n,m = map(int, input().split())

grid = [0] +  list(map(int, input().split()))

inf =-10

dp = [
    [inf]*(m+1)
    for _ in range(n+1)
]


dp[0][0] = 0

for i in range(1,n+1) :
    for j in range(m+1) :
        if grid[i] < 0 :
            if dp[i-1][j-1] != inf :
                dp[i][j] = max(dp[i-1][j-1] + grid[i],dp[i][j])
        
        else :
            if dp[i-1][j] != inf :
                dp[i][j] = max(dp[i-1][j] + grid[i],dp[i][j])

print(dp)