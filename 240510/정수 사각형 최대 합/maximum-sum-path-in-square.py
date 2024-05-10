import sys

input = sys.stdin.readline


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]


dp = [[0]* n for _ in range(n)]


dp[0][0] = matrix[0][0]


for i in range(1,n) :
    dp[i][0] = matrix[i][0] + dp[i-1][0]


for i in range(1,n) :
    dp[0][i] = matrix[0][i] + dp[0][i-1]




for i  in range(n) :
    for j in range(n) :
        if dp[i][j] != 0 :
            continue
        
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + matrix[i][j]



print(dp[n-1][n-1])