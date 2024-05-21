n =  int(input())


grid = [list(map(int,  input().split())) for _ in range(n)]



max_block  = 1
max_block_count = 0

def in_range(x,y) :
    return 0 <= x < n  and 0 <= y < n 


def can_go(x,y) :
    if not in_range(x,y) :
        return False
    
    if visited[x][y] or new_grid[x][y] == 0 :
        return False
    
    return True

def dfs(x,y) :
    dxs, dys = [-1,0,1,0] , [0,1,0,-1]

    for dx, dy in zip (dxs, dys) :
        new_dx , new_dy = x + dx , y +dy

        if can_go(new_dx,new_dy) :
            visited[new_dx][new_dy] = 1
            answer[new_dx][new_dy]  = order
            dfs(new_dx,new_dy)



for num in range(1,101) :
    order = 1
    answer    =     [[0]*n for _ in range(n)]
    visited   =     [[0]*n for _ in range(n)]
    new_grid =      [[0]*n for _ in range(n)]

    for r in range(n) :
        for c in range(n) :
            if grid[r][c] == num :
                new_grid[r][c] = 1
            else :
                new_grid[r][c] = 0
    
    for r in  range(n) :
        for c in range(n) :
            if can_go(r,c) :
                visited[r][c] = 1
                answer[r][c] = order
                dfs(r,c)
                order +=1

    order_list = [0]*(order+1)
    for o in range(1,order+1) :

        for r in range(n) :
            for c in range(n) :
                if answer[r][c] == o :
                    order_list[o] +=1

    result_list = []
    maxi_result = max(order_list)
    for result in order_list :
        if result >=4 :
            max_block_count += 1
    
    max_block = max(max_block, maxi_result)


print(max_block_count,max_block)