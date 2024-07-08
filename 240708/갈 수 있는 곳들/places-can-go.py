from collections import deque



n,k = map(int, input().split())


grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
q = deque()


def in_range(x,y) :
    return  0<= x < n and 0 <= y < n 


order = 0


def can_go(x,y) :
    if not in_range(x,y) :
        return False

    if visited[x][y] == True or grid[x][y] == 1 :
        return False

    return True


def push(x,y) :
    global order
    order +=1
    q.append((x,y))
    visited[x][y] = True


def bfs() :
    dxs = [-1,1,0,0] #상하좌우
    dys = [0,0,-1,1]
    while q :
        x,y = q.popleft()

        for dx, dy in zip (dxs, dys) :
            new_x, new_y = x +dx , y +dy
            if can_go(new_x,new_y) :
                push(new_x,new_y)


for _ in range(k) :
    x_grid, y_grid = map(int, input().split())

    push(x_grid-1,y_grid-1)
    bfs()


print(order-1)