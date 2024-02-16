import sys

input = sys.stdin.readline

dxs = [-1,0,1,0]
dys = [0,1,0,-1]


n, m = map(int, input().split())

matrix = [[0 for _ in range(n)] for i in range(n)]


info = [list(map(int, input().split())) for _ in range(m)]


def checking(x,y,n) :
    return  0 <= x < n and 0<= y < n 


for element in info :
    count = 0
    r = element[0] -1
    c = element[1] -1 

    matrix[r][c] = 1

    for dir_num in range(4) :
        nr, nc = r + dxs[dir_num], c + dys[dir_num]

        if checking(nr,nc,n) and matrix[nr][nc] :
            count +=1
    
    if count == 3:
        print(1)
    else :
        print(0)