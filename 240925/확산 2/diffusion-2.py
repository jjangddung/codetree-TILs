from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
# print(1)

grid = [list(map(int, input().split()))
        for _ in range(n)
    ]


visited = [
    [False] *(m)
    for _ in range(n)
]
step = [
    [-1 for _ in range(m)]
    for _ in range(n)
]

q = deque()

def in_range(x,y) :
    return 0 <= x< n and 0 <= y < m


def can_go(x,y) :

    if in_range(x,y)  :

        if grid[x][y] != -1 :
            return True
    
    return False



def push(x,y,s) :
    q.append((x,y))
    visited[x][y] = True
    step[x][y] = s

one_lst = []
minus_lst = []
for i in range(n) :
    for j in range(m) :
        if grid[i][j] == 1 :
            one_lst.append([i,j])
        if grid[i][j] == -1 :
            minus_lst.append([i,j])

def bfs() :
    dxs, dys = [-1,0,1,0], [0,1,0,-1]
    while q :
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            new_x, new_y = x + dx, y  + dy

            if can_go(new_x, new_y) and not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y] +1)


    
for g in one_lst :
    x,y = g[0], g[1]

    push(x,y,0)

bfs()

maxi = -sys.maxsize
count = 0
for i in range(n) :
    for j in range(m) :
        t = [i,j]
        maxi = max(step[i][j], maxi)
        if grid[i][j] == -1 :
            if t not in minus_lst :
                count +=1

if count == 0 :
    print(maxi)

else :
    print(-1)