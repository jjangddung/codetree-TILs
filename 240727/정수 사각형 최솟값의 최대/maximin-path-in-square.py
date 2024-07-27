n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]





dp = [[0]*n for _ in range(n)]

dp[0][0] = matrix[0][0]

for i in range(1,n) :
    dp[0][i] = min(dp[0][i-1],matrix[0][i])



for j in range(1,n) :
    dp[j][0] = min(dp[j-1][0], matrix[j][0])




for i  in range(n) :
    for j in range(n) :
        if i == 0 or j == 0 :
            continue

        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]),matrix[i][j])


print(dp[n-1][n-1])