import sys


input  = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]



dp =  [[0]*n for _ in range(n)]


dp[0][n-1] =  matrix[0][n-1]
for i in range(1,n) :
    dp[0][n-1-i] =dp[0][n-i] + matrix[0][n-1-i]


# print(*dp)

for i in range(1,n) :
    dp[i][n-1] = dp[i-1][n-1] + matrix[i][n-1]

# print(*dp)


for i in range(n) :
    for j in range(n-1,-1,-1) :
        if i == 0 or j == n-1 :
            continue

        dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + matrix[i][j]



print(dp[n-1][0])