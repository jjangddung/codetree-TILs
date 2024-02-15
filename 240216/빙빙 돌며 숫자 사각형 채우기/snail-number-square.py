import sys


input = sys.stdin.readline
n,m = map(int, input().split())



arr = [[0 for i in range(m)] for _ in range(n)]



dxs = [-1,0,1,0] # 0,1,2,3 >>> 위 오 아 왼
dys = [0,1,0,-1]

first_dir =  1


def checking (x,y,n,m) :
    return 0 <= x < n and 0 <= y < m 


x, y = 0 , 0
start = 2
arr[x][y] = 1
# print(t)

for i in range(2, n*m +1) :

    nx, ny = x + dxs[first_dir], y + dys[first_dir]

    # print(nx,ny)

    if  not checking(nx,ny,n,m)  or arr[nx][ny] != 0 :
        first_dir = (first_dir+1) % 4
    
    x, y = x + dxs[first_dir], y + dys[first_dir]
    arr[x][y] = i


for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = " ")
    print()