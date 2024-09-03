from collections import deque

n,h,m  = map(int, input().split())


grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = [
    [0 for _ in range(n)]
    for i in range(n)
]


def push(x,y,s) :
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))


def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n

def can_go(x,y) :
    if in_range(x,y) :
        if grid[x][y] == 0 or grid[x][y] == 3 :
            return True
    return False


def bfs() :
    dxs,dys = [-1,0,1,0] , [0,1,0,-1] # 상하좌우
    while q :
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys) :
            new_x, new_y = x + dx, y +dy
            if can_go(new_x,new_y)  and  not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y] +1 )

no_rain = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 3 :
            no_rain.append([i,j])

for i in range(n) :
    for j in range(n) :
        if grid[i][j] != 2 :
            continue
        q= deque()
        visited = [
            [False for _ in range(n)]
            for i in range(n)
        ]

        step = [
            [0 for _ in range(n)]
            for i in range(n)
        ]
        push(i,j,0)
        bfs()
        maxi = -1

        for v in no_rain :
            result = step[v[0]][v[1]]
            maxi = max(result, maxi)
        if maxi == 0 :
            answer[i][j] = -1
        else :
            answer[i][j] = maxi

for ans in answer :
    print(*ans)