import sys

n = int(input())
dp = [0]*(1001)

dp[0] = 1
dp[1] = 1
dp[2] = 3
# dp[3] = dp[2] + 3 *dp[1]

# dp[i] = dp[i-1] + 3*dp[i-2]


for i in range(3,n+1) :
    dp[i] = dp[i-1] + 2*dp[i-2]
    dp[i] = dp[i]%10007

print(dp[n])