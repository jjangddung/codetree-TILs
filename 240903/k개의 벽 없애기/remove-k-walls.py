from collections import deque
import copy
import sys


n,k = map(int, input().split())


grid = [
    list(map(int ,input().split()))
    for _ in range(n)
]

r1,c1 = map(int, input().split())
r2,c2 = map(int, input().split())
r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1


wall_list = []
ans = []
count = 0

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 :
            wall_list.append([i,j])
            count +=1



def push(x,y,s) :
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def in_range(x,y) :
    return 0<=x < n and 0 <=y < n 

def can_go(x,y) :
    if in_range(x,y) and new_grid[x][y] == 0 :
        return True
    
    return False


def bfs() :
    dxs,dys = [-1,0,1,0], [0,1,0,-1] # 12시부터 시계방향

    while q :
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys) :
            new_x, new_y = x +dx , y + dy
            if can_go(new_x,new_y) and not visited[new_x][new_y]  :
                push(new_x,new_y,step[x][y]+1)


result = sys.maxsize





def backtracking(start,num) : # 서로 다른 n개에서 중복없이 k개 뽑기
    global result
    global visited
    global step
    global q
    global new_grid
    if num == k :
        new_lst = copy.deepcopy(ans)
        new_grid = copy.deepcopy(grid)
        q = deque()
        visited = [
            [False for _ in range(n)]
            for _ in range(n)
        ]
        step = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        for dest_pos in new_lst :
            dest_x, dest_y = wall_list[dest_pos]
            new_grid[dest_x][dest_y] = 0

        push(r1,c1,0)
        bfs()
        if step[r2][c2] != 0 : 
            result = min(result,step[r2][c2])
        # print(ans)
        return 
    
    for i in range(start,count) :
        ans.append(i)
        backtracking(i+1,num+1)
        ans.pop()

backtracking(0,0)

if result == sys.maxsize :
    print(-1)
else :
    print(result)