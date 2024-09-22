import sys

n= int(input())

INT_MIN = -sys.maxsize
grid = [0] + list(map(int, input().split()))



# dp[i][j] i번째까지의 계단도달 >>> (무조건 도달임) 이때   j번만큼 1칸씩 움직였을 때의 최대 동전 개수

# 한 칸씩만 움직이는 경우 dp[i][j] = max(dp[i-1][j-1] + grid[i], dp[i][j])
# 두 칸씩만 움직이는 경우 dp[i][j] = max(dp[i-2][j] + grid[i], dp[i][j])




dp = [
    [INT_MIN]*(4)
    for _ in range(n+1) 
]


for i in range(4) :
    dp[0][i] = 0


def in_range(x,y) :
    return 0 <= x <= n and 0 <= y < 4 

# print(grid)
# print(dp)
# print(dp[4][1])
maxi = -sys.maxsize
for i in range(1,n+1) :
    for j in range(4) :
        if not in_range(i-1,j-1) :
            continue 
        print(i,j)
        dp[i][j] = max(dp[i-1][j-1] + grid[i], dp[i][j])

        if not in_range(i-2,j) :
            continue

        dp[i][j] = max(dp[i-2][j] + grid[i], dp[i][j])

        maxi = max(maxi, dp[i][j])

print(maxi)