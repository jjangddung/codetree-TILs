import sys


INT_MIN = -sys.maxsize


n =  int(input())

grid = list(map(int, input().split()))

grid = [0] + grid

dp = [INT_MIN]*(n+1)

dp[1] = grid[1]

dp[0] = 0


maxi = INT_MIN
for i in range(1,n+1) :
    dp[i] = max(dp[i-1]+grid[i], grid[i])
    # print(dp[i])
    maxi = max(maxi,dp[i])


print(maxi)