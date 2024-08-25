from collections import deque





n,m,k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def transmition(grid) :
    for i in range(n) :
        for j in range(i,n) :
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]



transmition(grid)

mini = 10000
maxi_index = 0
for i in range(n) :
    if k-1 <= i < k-1+m :
        for l in range(n) :
            if grid[i][l] != 0 :
                if l-1 < mini :
                    mini = l-1
                break


# print(mini)


if n != 1 :
    for i in range(n) :
        
        if k-1 <= i < k-1+m :
            grid[i][mini] =1
    
    
    transmition(grid)
    for g in grid :
        print(*g)
else :
    print(1)