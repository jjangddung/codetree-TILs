n,m = map(int , input().split())

order = 1
# print(n,m)

matrix = [list(map(int , input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
answer =  [[0]*m for _ in range(n)]

def in_range(r,c) :
    return 0 <= r < n and 0 <= c < m

def can_go(x,y) :
    if not in_range(x,y) :
        return False
    
    if visited[x][y] or matrix[x][y]  == 0 :
        return False
    
    return True




def dfs(x,y) :
    global order

    dxs = [-1,0] # 하 우
    dys = [0,1]

    for dx , dy in zip(dxs, dys) :
        new_x, new_y = x + dx , y +dy
        
        if can_go(new_x,new_y) :
            answer[new_x][new_y] = order
            order +=1
            visited[new_x][new_y] = 1
            dfs(new_x,new_y)

answer[0][0] = order
order = 1
visited[0][0] = 1
dfs(0,0)

if answer[n-1][m-1] != 0 :
    print(1)

else :
    print(0)