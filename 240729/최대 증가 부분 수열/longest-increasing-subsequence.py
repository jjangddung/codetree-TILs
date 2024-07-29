import sys
INT_MIN = -sys.maxsize

n = int(input())


matrix = list(map(int, input().split()))

dp = [0] *n

for i in range(n) :
    dp[i] = INT_MIN


dp[0] = 1


for i in range(1,n) :
    for j in range(i) :

        if dp[j] == INT_MIN :
            continue

        if matrix[i] > matrix[j] :
            dp[i] = max(dp[i], dp[j] + 1,1)





print(max(dp))