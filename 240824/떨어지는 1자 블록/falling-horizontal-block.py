from collections import deque





n,m,k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def transmition(grid) :
    for i in range(n) :
        for j in range(i,n) :
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]



transmition(grid)

maxi = 0
maxi_index = 0
for i in range(n) :
    total = sum(grid[i])
    if k-1 <= i < k-1+m :
        if maxi < total :
            maxi_index = i
            maxi = total
    

for i in range(n) :
    
    if k-1 <= i < k-1+m :
        grid[i][n-1-maxi] =1


transmition(grid)

for g in grid :
    print(*g)