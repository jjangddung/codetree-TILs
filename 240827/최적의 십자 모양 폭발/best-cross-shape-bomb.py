import copy


n = int(input())


grid = [list(map(int, input().split())) for _ in range(n)]

dxs,dys = [-1,0,1,0], [0,1,0,-1] # 상우하좌
cxs, cys = [0,1],[1,0] # 우하

def cango(x,y) :
    return 0 <=x < n and 0 <= y < n




def transmition(grid) :
    for i in range(n) :
        for j in range(i,n) :
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]



def gravity(grid) :
    real_grid = []
    for lst in grid :
        new_lst = []

        for l in lst :
            if l != 0 :
                new_lst.append(l)

        new_lst = [0]*(n-len(new_lst)) + new_lst
        
        real_grid.append(new_lst)
    
    
    return real_grid



        



def bomb(x,y,new_grid) :
    power = new_grid[x][y]

    new_grid[x][y] = 0

    for dx, dy in zip(dxs, dys) :
        for p in range(1,power) :
            new_x, new_y = x  + dx*p , y + dy*p
            if cango(new_x,new_y) :
                new_grid[new_x][new_y] = 0

    transmition(new_grid)
    new_grid= gravity(new_grid)
    transmition(new_grid)

    point = 0

    for i in range(n) :
        for j in range(n) :
            if new_grid[i][j] == 0 :
                continue
            for cx ,cy in zip(cxs,cys) :
                new_x, new_y = i + cx, j +cy
                if cango(new_x,new_y) :
                    if new_grid[i][j] == new_grid[new_x][new_y] :
                        point +=1 
    return point


point = 0 

for i in range(n) :
    for j in range(n) :
        new_grid = copy.deepcopy(grid)
        result = bomb(i,j,new_grid)
        # print("result: ",result)
        point = max(point, result)
        


print(point)