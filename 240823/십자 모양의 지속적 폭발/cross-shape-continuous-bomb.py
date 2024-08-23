import sys

input= sys.stdin.readline

n, m = map(int, input().split())

grid=  [list(map(int , input().split())) for _ in range(n)]

def can_go(x,y) :
    return 0 <= x < n and 0 <= y < n



def bomb(r,c) :
    count = grid[r][c]
    count -=1
    grid[r][c] = 0

    dxs= [-1,0,1,0] # 상우하좌
    dys= [0,1,0,-1] 


    for dx, dy in zip(dxs,dys) :
        for i in range(1,count+1) :
            new_x, new_y = r + dx*i , c +dy*i
            if can_go(new_x,new_y) :
                grid[new_x][new_y] = 0
    
    # print(*grid)



def filter(grid) :
    new_grid = []

    for lst in grid :
        new_lst= []
        lst= lst[::-1]

        for v in lst :
            if v != 0 :
                new_lst.append(v)
        new_lst = new_lst + [0]*(n - len(new_lst))
        new_lst = new_lst[::-1]
        new_grid.append(new_lst)
    
    return new_grid

        


def transimition(grid) :
    for i in range(n) :
        for j in range(i,n) :
            grid[i][j],grid[j][i]= grid[j][i] , grid[i][j]

    return grid




for _  in range(m) :
    c = int(input())
    c-=1
    num = -1


    for i in range(n) :
        if grid[i][c] != 0 :
            num = i
            break
    # print(i,c)

    if num == -1 :
        continue
    
    bomb(num,c)
    grid = transimition(grid)
    grid = filter(grid)
    grid = transimition(grid)


for g in  grid :
    print(*g)