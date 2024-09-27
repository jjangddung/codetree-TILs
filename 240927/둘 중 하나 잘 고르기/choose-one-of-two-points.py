import sys

n = int(input())


grid = [
    list(map(int, input().split()))
    for _ in range(2*n)
]

grid = [[0,0]] + grid

# print(grid)


# dp의 정의를 어떻게 ????? dp[i][j] >>> i번째까지 고른 카드중 j만큼의 빨간색 카드 ???

# 0 < = i <= 2* n
inf = -sys.maxsize


dp = [
    [inf] * (n+1)
    for _ in range(2*n +1 )
]


dp[0][0] = 0 
maxi = -sys.maxsize



for i in range(1,2*n + 1) :
    for j in range(n+1) :
        if abs(i-j) > n :
            continue
        if dp[i-1][j-1] != inf :
            dp[i][j] = max(dp[i-1][j-1] + grid[i][0], dp[i][j])
        
        if dp[i-1][j] != inf :
            dp[i][j]  = max(dp[i-1][j] + grid[i][1],dp[i][j] )
        maxi = max(dp[i][j], maxi)


# print(dp)
print(maxi)