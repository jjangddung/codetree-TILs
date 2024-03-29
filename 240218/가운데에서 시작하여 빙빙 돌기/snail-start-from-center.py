import sys

input = sys.stdin.readline


n = int(input())

matrix = [[0 for _ in  range(n)] for i in range(n)]


dxs = [0,-1,0,1] # left up right down
dys = [-1,0,1,0]


dir = 0


x,y = n-1  , n-1 


matrix[x][y] = n*n

def in_range(x,y) :
    return 0 <=x < n and 0 <= y < n


for i in range(1,n*n) :
    nx , ny = x + dxs[dir] , y +dys[dir]

    if not in_range(nx,ny) or matrix[nx][ny] != 0 :
        dir = (dir +1) % 4
    
    x, y = x + dxs[dir], y +dys[dir]
    matrix[x][y] = n*n - i

for i in range(n) :
    for j in range(n) :
        print(matrix[i][j], end= " ")
    print()