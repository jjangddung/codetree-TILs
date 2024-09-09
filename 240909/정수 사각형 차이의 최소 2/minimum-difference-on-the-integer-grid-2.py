import sys


n = int(input())

grid =[
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [1,0],[0,1] # 하 우


dp = [
    [-1]*n
    for _ in range(n)
]





dp[0][0] = grid[0][0]


# dp를 3차원으로 구현

# 최댓값을 최소로 하는 쪽으로 움직임

mini = [
    [101]*n
    for _ in range(n)
]

mini[0][0]= grid[0][0]



for i in range(1,n) :
    dp[0][i] = max(dp[0][i-1],grid[0][i])
    mini[0][i] = min(mini[0][i-1],grid[0][i])


for i in range(1,n) :
    dp[i][0] = max(dp[i-1][0],grid[i][0])
    mini[i][0] = min(mini[i-1][0],grid[i][0])

minimum_value = sys.maxsize

for i in range(1,n) :
    for j in range(1,n):

        dp[i][j] = min(dp[i-1][j],dp[i][j-1])

        if dp[i][j] == dp[i][j-1] :
            mini[i][j] = min(grid[i][j],mini[i][j-1])
        
        else :
            mini[i][j] = min(grid[i][j], mini[i-1][j])

        dp[i][j] = max(dp[i][j],grid[i][j])



result = dp[n-1][n-1] - mini[n-1][n-1]

print(result)