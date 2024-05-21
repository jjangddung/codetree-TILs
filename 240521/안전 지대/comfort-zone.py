n ,m  = map(int , input().split())


grid = [list(map(int, input().split())) for _ in range(n)]

result = 0
result_index = 0

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < m 


def can_go(x,y) :
    if not in_range(x,y) :
        return False
    
    if visited[x][y] == 1 or new_grid[x][y] == 0 :
        return False
    
    return True


def dfs(x,y) :
    global order
    dxs , dys = [-1,0,1,0] , [0,1,0,-1] # 상우하좌
    
    for dx , dy in zip(dxs,dys) :
        new_dx, new_dy = x + dx , y +dy

        if can_go(new_dx,new_dy) :
            visited[new_dx][new_dy] = 1
            answer[new_dx][new_dy] = order
            dfs(new_dx,new_dy) 


for p in range(1,101) :
    new_grid = [[0]*m for _ in range(n)]
    visited = [[0]* m for _ in range(n)]
    answer = [[0]* m for _ in range(n)]
    total_sum = 0
    order = 1

    for r in range(n) :
        for c in range(m) :
            if grid[r][c] <= p :
                new_grid[r][c] = 0
            else :
                new_grid[r][c] = 1
            total_sum  += new_grid[r][c]
    if total_sum == 0 :
        break 
    
    for r in range(n) :
        for c in range(m) :
            if can_go(r,c) :
                visited[r][c]  = 1
                answer[r][c] = order
                dfs(r,c)
                order +=1
    
    if order > result :
        result_index = p
        result =  order
        



print(result_index , result - 1)