# dp[i] 


import sys

n = int(input())


dp = [0]*(20)

# dp[i] = sigma(dp[k]* dp[i-k-i])
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5
#dp[3] =  dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]


for i in range(4,n+1) :
    total = 0
    for k in range(0,i+1):
        total += (dp[k]*dp[i-k-1])
    
    dp[i] = total


print(dp[n])