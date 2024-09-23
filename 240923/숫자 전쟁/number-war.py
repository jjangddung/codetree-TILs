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
        if b[i-1] < a[j] :
            if dp[i-1][j] == -1 :
                continue
            dp[i][j] = max(dp[i-1][j],dp[i][j])

        elif b[i-1] == a[j] :
            dp[i][j] =-1
            continue

        if b[i] > a[j-1] :
            if dp[i][j-1] == -1 :
                continue
                
            dp[i][j] = max(dp[i][j-1],dp[i][j])

        elif b[i] == a[j-1] :
            dp[i][j] = -1
            continue

        if b[i] < a[j] :
            dp[i][j] = dp[i][j] + b[i]

            if i == n :
                maxi = max(dp[i][j], maxi)
            
        elif b[i] > a[j] :
            if j == n :
                maxi = max(dp[i][j], maxi)
        
        else :
            if j == n or i == n :
                maxi = max(dp[i][j], maxi)

        
        

    
print(maxi)
print(dp)
#