from collections import deque


n = int(input())


# bfs로 구현하면 될듯..?

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = [
    [0]*n
    for _ in range(n)
]

def in_range(x,y) :
    return 0 <=x < n and 0 <= y < n


def push(x,y,s) :
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))


def can_go(x1,y1,x2,y2) :
    if in_range(x2,y2) and grid[x2][y2] > grid[x1][y1] :
        return True
    
    return False

visited = [
    [False]*n
    for _ in range(n)
]


step = [
    [0]*n
    for _ in range(n)
]





def bfs() :
    dxs, dys = [-1,0,1,0],[0,1,0,-1] # 시계방향
    maxi = 0

    while q :
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            new_x, new_y = x + dx, y + dy

            if can_go(x,y,new_x,new_y) and not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y]+1)
                maxi = max(maxi,step[x][y]+1)
    
    return maxi

q = deque()
final = 0
for i in range(n) :
    for j in range(n) :
        for a in range(n) :
            for b in range(n):
                visited[a][b] = False
                step[a][b] = 0
        push(i,j,0)
        result = bfs()
        final = max(result,final)


print(final+1)