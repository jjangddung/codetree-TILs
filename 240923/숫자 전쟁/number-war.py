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
        count1,count2,count3,count4 = 0,0,0,0

        if b[i-1] < a[j] :
            dp[i][j] = max(dp[i-1][j],dp[i][j])
            count1 +=1
        
        if b[i]  > a[j-1] :
            dp[i][j] = max(dp[i][j-1],dp[i][j])
            count2 += 1
        
        if count1 == 0 and count2 == 0 :
            if b[i-1] == a[j] :
                dp[i][j] = dp[i-1][j]
            
            if b[i] == a[j-1] :
                dp[i][j] = dp[i-1][j]
                
        
        dp[i][j] = max(dp[i-1][j-1],dp[i][j])
        
        if a[j] > b[i] :
            
            dp[i][j] = dp[i][j] + b[i]

            if i == n :  
                maxi = max(maxi, dp[i][j])
        
        else :
            if i==n or j  == n :
                maxi = max(maxi, dp[i][j])



print(maxi)