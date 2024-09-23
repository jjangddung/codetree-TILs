import sys


n,m = map(int, input().split())

grid = [0] +  list(map(int, input().split()))

inf =-sys.maxsize

dp = [[[inf for _ in range(m+1)] for _ in range(n+1)] for _ in range(n+1)]

dp[0][0][0] = 0

maxi = -sys.maxsize

for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(m+1) :
            if grid[j] < 0 :
                if k-1 >= 0 :
                    if dp[i-1][j-1][k-1] == inf :
                        continue
                    dp[i][j][k] = max(dp[i-1][j-1][k-1] + grid[j], dp[i][j][k])
            
            else :
                if dp[i-1][j-1][k] == inf :
                        continue
                dp[i][j][k] = max(dp[i-1][j-1][k] + grid[j], dp[i][j][k])
            
            maxi = max(dp[i][j][k], maxi)

print(maxi)
# print(dp)