import sys

n = int(input())

a = [0] +  list(map(int, input().split()))
b = [0] +  list(map(int, input().split()))


dp = [
    [-1]*(n+1)
    for _ in range(n+1)
]

for i in range(n+1) :
    dp[i][0] = 0
    dp[0][i] = 0


maxi = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :

        if a[j-1] == b[i] or b[i-1] == a[j] :
            continue
            
        if b[i-1] <= a[j] :
            dp[i][j] = max(dp[i-1][j],dp[i][j])
        
        if b[i]  >= a[j-1] :
            dp[i][j] = max(dp[i][j-1],dp[i][j])
        
        dp[i][j] = max(dp[i-1][j-1],dp[i][j])
        
        if a[j] > b[i] :
            
            dp[i][j] = dp[i][j] + b[i]

            if i == n :  
                maxi = max(maxi, dp[i][j])
        
        else :
            if i==n or j  == n :
                maxi = max(maxi, dp[i][j])



print(maxi)