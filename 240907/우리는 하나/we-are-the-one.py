import sys
from collections import deque
import copy

# 백트래킹으로 서로 다른 k개 뽑기
# 갈 수 있는 도시 수 뽑기


n,k,u,d = map(int, input().split())

grid= [
    list(map(int, input().split()))
    for _ in range(n)
]

# print(*grid)


back_lst = []
ans_lst = []
q = deque()
def backtracking(num,t) :
 
        
    if num == n**2 :
        if len(back_lst) == k :
            ans = copy.deepcopy(back_lst)
            ans_lst.append(ans)
            # print(back_lst)
        return
            
    
    back_lst.append(num)
    backtracking(num+1,t+1)
    back_lst.pop()
    backtracking(num+1,t)

    return 

backtracking(0,0)

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n 

def can_go(x1,y1,x2,y2) :
    if in_range(x2,y2) :
        result = abs(grid[x1][y1] - grid[x2][y2])
        if u <= result <= d :
            return True
    
    return False

def push(x,y,s) :

    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))




def bfs() :
    dxs, dys = [-1,0,1,0],[0,1,0,-1] # 상우하좌

    while q :
        x,y= q.popleft()
        for dx, dy in zip(dxs, dys) :
            new_x, new_y = x + dx, y+ dy
            if can_go(x,y,new_x,new_y) and not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y]+1)
final  = 0

for value in ans_lst :
    visited = [
        [False]*n
        for _ in range(n)
    ]
    # print(visited)
    step  = [
        [0]*n
        for _ in  range(n)
    ]
    for i in range(k) :
        x = value[i]//n
        y = value[i]%n
        push(x,y,0)
    bfs()
    count = 0

    for i in range(n) :
        for j in range(n) :
            # print(i,j)
            if visited[i][j] :
                count +=1
    
    final = max(count, final)

print(final)