import sys


INT_MIN = -sys.maxsize

n = int(input())

grid = [0] + list(map(int, input().split()))


OFFSET = 100000

m = sum(grid)

dp = [
    [0]*(m+1+OFFSET)

    for _ in range(n+1)
]

def init() :
    for i in range(n+1) :
        for j in range(-m,m+1) :
            dp[i][j+ OFFSET] =  INT_MIN

    
    dp[0][0 + OFFSET] = 0



def update(i,j,prev_i,prev_j,val) :

    if prev_j < -m or prev_j > m or dp[prev_i][prev_j] == INT_MIN :
        return 
    
    dp[i][j+ OFFSET] = max(dp[i][j+OFFSET], dp[prev_i][prev_j+ OFFSET] + val)



init()

for i in range(1,n+1) :
    for j in range(-m,m+1) :
        

        update(i,j,i-1,j-grid[i],grid[i])
        update(i,j, i-1,j + grid[i], 0)


if dp[n][0+OFFSET] > 0 :
    print("Yes")

else :
    print("No")