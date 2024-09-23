import sys


n,m = map(int, input().split())

grid = [0] +  list(map(int, input().split()))

# dp[i][j]  i개를 연속해서 골랐을 때, 음수의 개수가 j개일때의 최대값

dp = [
    [-1]*(3)
    for _ in range(n+1)
]


dp[0][0] = 0

maxi = -sys.maxsize
for i in range(1,n+1) :
    for j in range(m+1) :
        for k in range(1,n+2-i): 
            new_lst = grid[k:i+k]
            count = 0
            result = 0
            for v in new_lst :
                if v < 0 :
                    count +=1
                result += v
            
            if count == j :
                dp[i][j] = max(dp[i][j], result)
                maxi = max(dp[i][j],maxi)

print(maxi)
# print(dp)