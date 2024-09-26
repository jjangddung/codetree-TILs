import sys

n,k = map(int, input().split())



grid = [0] + list(map(int, input().split()))

# dp 정의를 어떻게 ?? 
# dp[i][j] ===     i번째를 포함할 때 j만큼의 음수를 가질때 최대의 크기
inf = -sys.maxsize



dp = [
    [inf] * (k+1)
    for _ in range(n+1)
]


dp[0][0] = 0

if grid[1] >= 0 :
    dp[1][0] = grid[1]

else :
    dp[1][1] = grid[1]

maxi = inf

for i in range(1,n+1) :
    for j in range(k+1) :
        if grid[i] >= 0   and dp[i-1][j] != inf:
            dp[i][j] = max(dp[i-1][j] + grid[i], dp[i][j])
        
        if grid[i] < 0 and j >= 1 and dp[i-1][j-1] != inf :
            dp[i][j] = max(dp[i-1][j-1] + grid[i], dp[i][j] )
        
        maxi = max(dp[i][j], maxi)

print(maxi)