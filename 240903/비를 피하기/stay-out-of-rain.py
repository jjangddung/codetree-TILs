from collections import deque

n,h,m  = map(int, input().split())

#비가  안내리는 곳에서 사람의 위치를 뿌려줌


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
    if in_range(x,y) and grid[x][y] != 1 :
        return True
    return False


def bfs() :
    dxs,dys = [-1,0,1,0] , [0,1,0,-1] # 상우하좌
    while q :
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys) :
            new_x, new_y = x + dx, y +dy
            if can_go(new_x,new_y)  and  not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y] +1 )

human = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 2 :
            human.append([i,j])
            answer[i][j] = -1

no_rain = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 3 :
            no_rain.append([i,j])

for pos in no_rain :
    x,y =pos[0],pos[1]

    q= deque()
    visited = [
        [False for _ in range(n)]
        for i in range(n)
    ]
    step = [
        [0 for _ in range(n)]
        for i in range(n)
    ]
    push(x,y,0)
    bfs()

    for h_pos in human :
        hx,hy = h_pos[0],h_pos[1]
        
        if answer[hx][hy] <= 0 :
            if step[hx][hy] != 0 :
                answer[hx][hy] = step[hx][hy]
            
            else :
                answer[hx][hy] = -1
        
        else :
            answer[hx][hy] = min(answer[hx][hy], step[hx][hy])
        


for ans in answer :
    print(*ans)