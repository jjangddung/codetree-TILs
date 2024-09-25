import sys



n,m = map(int, input().split())



grid = [
    list(map(int, input().split()))
    for _ in range(n)
]



def in_range(x,y) :
    return 0 <= x< n and 0 <= y < n



def can_go(x,y) :
    if not in_range(x,y) :
        return False
    
    return True

dxs,dys = [-1,-1,-1,0,1,1,1,0], [-1,0,1,1,1,0,-1,-1]

for _ in range(m) :
    for i in range(1,n**2+1) :
        change = 0
        
        for j in range(n) :
            if change != 0 :
                continue
            for k in range(n) :
                if change != 0 :
                    continue
                maxi = -sys.maxsize
                max_x, max_y = -3,-3
                if grid[j][k] == i :
                    for dx, dy in zip(dxs, dys) :
                        new_x, new_y = j + dx , k + dy

                        if can_go(new_x,new_y) :
                            if maxi  < grid[new_x][new_y] :
                                maxi = grid[new_x][new_y]
                                max_x,max_y = new_x , new_y

                    grid[max_x][max_y], grid[j][k] = grid[j][k] , grid[max_x][max_y]
                    change +=1
                
        
        
for v in grid :
    print(*v)
        # print("-------------------------------")