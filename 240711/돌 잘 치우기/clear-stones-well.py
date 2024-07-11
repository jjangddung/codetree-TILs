# backtracking, bfs 함수 하나 씩 해서 구성하기

from collections import deque

n,k,m = map(int, input().split())


grid =[list(map(int, input().split())) for _ in range(n)]



block_count = 0
block_list = []

for x in range(n) :
    for y in range(n) :
        if grid[x][y] == 1 :
            block_count +=1
            block_list.append([x,y])

# print(block_count)

answer_list = []
answer = []

def choose(curr_num,one_cnt) :

    #종료 조건
    if curr_num == block_count  :
        if one_cnt == block_count - m :
            new_list = []
            for ele in answer :
                new_list.append(ele)
            answer_list.append(new_list)
                
        return

    answer.append(curr_num)
    choose(curr_num+1,one_cnt+1)
    answer.pop()

    choose(curr_num+1,one_cnt)

    

choose(0,0)
# print(answer_list)

def in_range(x,y) :
    return 0 <=x <n and 0 <= y < n


def can_go(x,y) :
    if not in_range(x,y) :
        return False

    if  visited[x][y] or new_grid[x][y] :
        return False

    return True

def bfs() :
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    global order
    

    while q :
        x,y =q.popleft()
        for dx, dy in zip(dxs, dys) :
            new_x, new_y = x + dx, y+dy

            if can_go(new_x,new_y) == True :
                push(new_x,new_y)
    



maxi_order  = 0
order = 0
def push(x,y) :
    q.append((x,y))
    visited[x][y] = True

rc_list = []
for _ in range(k) :
    r,c = map(int, input().split())
    rc_list.append([r,c])




q = deque()
for blocks in answer_list :   # index position
    visited = [[False]*n for _ in range(n)]
    count = 0
    
    #push(r,c)
    new_grid = [[0]*n for _ in range(n)]
    for t in blocks :
        x,y = block_list[t][0] , block_list[t][1]
        new_grid[x][y] = 1

    for rc in rc_list :
        r,c = rc[0],rc[1]
        r ,c = r-1 ,c-1
        push(r,c)
        bfs()

    for x in range(n) :
        for y in range(n) :
            if visited[x][y] :
                count +=1

    maxi_order = max(count, maxi_order) 


print(maxi_order)
# print(num)