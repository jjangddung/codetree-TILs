import sys

n = int(input())

grid = [list(map(int , input().split())) for _ in range(n)]

r,c = map(int, input().split())

r-=1
c-=1

dxs, dys = [-1,0,1,0], [0,1,0,-1] # 상우하좌

def can_go(x,y) :
    return  0 <= x < n and 0 <= y < n


def boomb(r,c) :
    num = grid[r][c]
    grid[r][c] = 0

    count = num-1

    for dx, dy in zip(dxs,dys) :
        d = 1
        while d <= count :
            new_x, new_y = r + d*dx , c + d*dy
            if can_go(new_x,new_y) :
                grid[new_x][new_y] = 0
                d +=1
            else :
                break


def filler() :
    count = 0
    for i in range(n) :
        for j in range(n-1) :

            if grid[j][i] != 0 and grid[j+1][i] == 0 :
                grid[j][i],grid[j+1][i] = grid[j+1][i] ,grid[j][i]
                count +=1
    return count


boomb(r,c)

while filler() != 0 :
    filler()
for _ in grid:
    print(*_)