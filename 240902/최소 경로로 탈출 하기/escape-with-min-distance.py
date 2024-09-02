from collections import deque


q = deque()

n,m = map(int, input().split())

grid = [list(map(int, input().split()))
        for _ in range(n)
    ]

# print(grid)


step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
def in_range(x,y) :
    return 0 <=x < n and 0 <= y < m


def can_go(x,y) :
    if in_range(x,y) and grid[x][y] == 1 :
        return True
    
    else :
        return False





def push(x,y,s) :
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs() :
    dxs,dys = [1,0,-1,0], [0,1,0,-1]

    while q :
        x,y = q.popleft()

        for dx, dy in zip(dxs,dys) :
            new_x,new_y = x +dx , y +dy

            if can_go(new_x,new_y) and not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y] +1)



push(0,0,0)
bfs()

result = step[n-1][m-1]

if result == 0 :
    print(-1)

else :
    print(result)