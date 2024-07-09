# 시작점으로부터 갈 수 있는 위치점 찾기
# 그 후 시작점에서 위치점 까지 갈 수 있는지 체크 >> 갈 수 있는 위치점이면 
# 해당하는 숫자 , 없으면 0을 기입
# dx, dy 테크닉 이용 상하좌우 움직으로 도달할 수 있는지 체크
# can_go 함수를 이용하여 checking하기 >>> 갈 수 있으면 true
# 만약에 갈 수 있는 곳이라면 그 곳의 value값이랑 x,y값을 max_value, result_x, result_y로 저장하기
# for문을 (k번 반복)
from collections import deque

n,k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

q = deque()

r,c = map(int,input().split())

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n


def can_go(x,y) :
    if not in_range(x,y) :
        return False
    
    if visited[x][y] or go_grid[x][y] == 0 :
        return False
    
    return True



def push(x,y) :
    q.append((x,y))
    visited[x][y] = True

def bfs() :
    dxs = [-1,1,0,0] #상하좌우
    dys = [0,0,-1,1] 
    while q :
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            new_x, new_y = x + dx, y + dy

            if can_go(new_x,new_y) :
                visited[new_x][new_y] = True
                q.append((new_x,new_y))




for _ in range(k) :
    
    visited = [[False]*n for _ in range(n)]
    go_grid = [[0]*n for _ in range(n)]
    push(r-1,c-1) 
    value = grid[r-1][c-1]
    go_grid[r-1][c-1] = 1
    count = 0

    for x in range(n) :
        for y in range(n) :
            if x == r-1 and y == c-1 :
                continue
            if grid[x][y] < value :
                go_grid[x][y] = 1
            
            else :
                go_grid[x][y] = 0

    bfs()
    count = 0
    for x in range(n) :
        for y in range(n) :
            if visited[x][y] == True :

                if x == r-1 and y == c-1:
                    continue
                if count == 0 :
                    max_value = grid[x][y]
                    result_x,result_y = x, y
                    count +=1
                
                if grid[x][y] > max_value :
                    max_value =  grid[x][y]
                    result_x, result_y = x, y
    
    r,c = result_x+1, result_y+1

                

print(r, c)