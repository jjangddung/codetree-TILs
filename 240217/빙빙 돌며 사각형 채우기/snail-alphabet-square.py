import sys

input = sys.stdin.readline


alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

n, m = map(int, input().split())

dxs = [0,1,0,-1] #right down left up
dys = [1,0,-1,0]

matrix = [[0 for _ in range(m)]for i in range(n)]

matrix[0][0] = "A"


def in_range(x,y) :
    return 0 <= x < n and 0 <= y < m 

dir = 0

x,y = 0 , 0
for i in range(1,n*m) :
    nx, ny = x+ dxs[dir] , y +dys[dir]

    if not in_range(nx,ny) or matrix[nx][ny] != 0 :
        dir =(dir+1) %4
    
    x , y = x + dxs[dir], y + dys[dir]

    i = i % 26

    matrix[x][y] = alphabet[i]

for i in range(n) :
    for j in range(m) :
        print(matrix[i][j], end= " ")
    print()