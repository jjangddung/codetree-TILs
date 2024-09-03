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
    if in_range(x,y) and grid[x][y] == 0 :
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


visited = [
            [False for _ in range(n)]
            for _ in range(n)
        ]

step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

q = deque()


def backtracking(start,num) : # 서로 다른 n개에서 중복없이 k개 뽑기
    global result
    if start == len(wall_list) :
        if num == k :
            for i in range(n) :
                for j in range(n) :
                    visited[i][j] = False
                    step[i][j] = 0
            push(r1,c1,0)
            bfs()

            if step[r2][c2] != 0 :
                result = min(result,step[r2][c2])

        return 

    x,y = wall_list[start]
    grid[x][y] = 0
    backtracking(start+1,num +1) # i에 해당하는 idx 를 추가함
    grid[x][y] = 1

    backtracking(start+1,num) # i에 해당하는 idx를 추가하지 않음
 



backtracking(0,0)

if result == sys.maxsize :
    print(-1)
else :
    print(result)