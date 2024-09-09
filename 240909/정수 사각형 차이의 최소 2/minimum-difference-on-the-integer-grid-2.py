import sys
import copy

n = int(input())

grid =[
    list(map(int, input().split()))
    for _ in range(n)
]


dp = [
    [-1]*n
    for _ in range(n)
]



maximum = 0
minimum = sys.maxsize

for i in range(n) :
    for j in range(n) :
        maximum = max(maximum,grid[i][j])
        minimum = min(minimum,grid[i][j])



def in_range(x,y) :
    return  0 <= x < n and 0 <= y < n



def checking(x,y) :
    if grid[x][y] < mini :
        return False
    
    return True


def initialize(mini) :
    for i in range(1,n) :
        if grid[0][i] > mini :
            dp[0][i] = max(dp[0][i-1],grid[0][i])
        
        else :
            dp[0][i] = 127
        
        if grid[i][0] > mini :
            dp[i][0] = max(dp[i-1][0],grid[i][0])
        
        else :
            dp[i][0] = 127
        
    




final = sys.maxsize

for mini in range(maximum,minimum-1,-1) :
    if grid[0][0] < mini :
        continue

    # if grid[i][j] == 127 :
        # continue
    
    for i in range(n) :
        for j in range(n) :
            if grid[i][j] < mini :
                dp[i][j] = 127
            
            else :
                dp[i][j] = -1

    dp[0][0] = grid[0][0]

    initialize(mini)

    # if mini == 20 :
        # for d in dp :
            # print(*d)

    

    for i in range(1,n) :
        for j in range(1,n) :

            if dp[i][j] == 127 :
                continue


            if dp[i-1][j] == dp[i][j-1] and dp[i-1][j] == 127 :
                dp[i][j] = 127
                continue
            dp[i][j] = min(dp[i-1][j],dp[i][j-1])
            
            dp[i][j] = max(dp[i][j],grid[i][j])

            # if mini == 20 :
                # print(f'i:{i},j:{j} ,dp: {dp[i][j]}')
    
    # if mini == 20 :
        # for d in dp :
            # print(*d)
    # 
    if mini > dp[n-1][n-1] :
        continue

    result = dp[n-1][n-1] - mini
    final = min(final,result)
    # print(mini,result,final)

print(final)