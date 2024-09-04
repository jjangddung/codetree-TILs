import sys
from collections import deque

# 0은 아무것도 없는 칸 , 1은 귤이 있는 칸 2는 상한 귤이 있는 칸



n,k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

step = [
    [0]*n
    for _ in range(n)
]

visited = [
    [False]*n
    for _ in range(n)
]

# print(step)

strange_lst = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 0 :
            step[i][j] = -1
        elif grid[i][j] == 1 :
            step[i][j] = -2
        
        else :
            step[i][j] = 0
            strange_lst.append([i,j])


def in_range(x,y) :
    return  0 <= x < n and 0 <= y < n

def can_go(x,y) :
    if in_range(x,y) and grid[x][y] != 0 :
        return True
    return False

def push(x,y,s) :
    step[x][y] =s 
    visited[x][y] = True
    q.append((x,y))

q = deque()

def bfs() :
    dxs, dys = [-1,0,1,0],[0,1,0,-1] # 12시부터 시계

    while q :
        x,y = q.popleft()
        for dx, dy in zip (dxs, dys) :
            new_x, new_y = x + dx,  y + dy
            if can_go(new_x,new_y) and not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y]+1)

for str_ora in strange_lst :
    x,y = str_ora
    push(x,y,0)

bfs()

for s in step :
    print(*s)