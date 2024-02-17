import sys

input = sys.stdin.readline


n,m = map(int, input().split())


matrix = [[0 for _ in range(m)] for i in range(n)]

dxs = [1,0,-1,0] # down right up left
dys = [0,1,0,-1]

x,y = 0, 0

dir = 0

matrix[0][0] = 1

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < m 

for i in range(2, n*m +1) :
    nx, ny = x + dxs[dir], y + dys[dir]
    if not in_range(nx,ny) or matrix[nx][ny] != 0 :
        dir = (dir+1) % 4
    
    x,y = x + dxs[dir], y +dys[dir]
    matrix[x][y] = i


for i in range(n) :
    for j in range(m) :
        print(matrix[i][j], end = " ")
    print()