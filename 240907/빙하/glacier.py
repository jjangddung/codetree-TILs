from collections import deque

import copy
import sys


n,m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]




def in_range(x,y) :
    return 0 <=x < n and 0 <= y < m

def can_go(x,y) :
    if in_range(x,y) and grid[x][y] != 1 :
        return True
    
    return False

def vist_ice(x,y,new_x,new_y) :
    if can_go(x,y) and not can_go(new_x,new_y) :
        return True
    
    return False


def push(x,y) :
    visited[x][y]= True
    q.append((x,y))

 
def bfs() :
    dxs, dys = [-1,0,1,0],[0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            new_x , new_y = x+ dx, y +dy
            if can_go(new_x,new_y)  :
                if not visited[new_x][new_y] :
                    push(new_x,new_y)
            else :
                if in_range(new_x,new_y) :
                    visited_ice[new_x][new_y] = True
            

first = True
Time = 0
# print("why?")
q = deque()

visited = [[False] * m for _ in range(n)]
visited_ice = [[False] * m for _ in range(n)]
# print("not: ", visited)

prev= 0
while first :
    
    Time +=1
    for i in range(n) :
        for j in range(m) :
            visited[i][j] = False
            visited_ice[i][j] = False
    # print(visited)
    push(0,0)
    # print("checking")
    bfs()
    # count = 0
    result = 0

    for i in range(n) :
        for j in range(m) :
            if visited_ice[i][j] :
                grid[i][j] = 0
                result +=1
    # print(Time, count)

    if result == 0 :
        result = prev
        first = False
    
    else :
        prev = result


print(Time-1, result)