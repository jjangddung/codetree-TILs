from collections import deque



n = int(input())

q = deque()

step = [
    [0 for _ in range(n)]
    for _ in range(n)
]


visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n





def push(x,y,s) :
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))


def bfs() :
    dxs = [-2,-1,1,2,2,1,-1,-2]  # 나이트의 움직임
    dys = [1,2,2,1,-1,-2,-2,-1]

    while q :
        x,y = q.popleft()

        for dx, dy in zip(dxs,dys) :
            new_x,new_y = x +dx , y +dy

            if in_range(new_x,new_y) and not visited[new_x][new_y] :
                push(new_x,new_y,step[x][y] +1)
    

r1,c1,r2,c2 = map(int, input().split())

push(r1-1,c1-1,0)
bfs()

result = step[r2-1][c2-1]

# print(*step)

if result == 0 :
    if r1==r2 and c1 == c2 :
        print(0)
    else :
        print(-1)

else :
    print(result)