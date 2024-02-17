import sys

input = sys.stdin.readline



n, t = map(int, input().split())


ori_order = input()


matrix = [list(map(int, input().split())) for _ in range(n)]



dxs = [-1,0,1,0] # up right down left
dys = [0,1,0,-1]

dir = 0

k = 1



def in_range(x,y) :
    return 0 <=x < n and 0 <= y < n

x,y = n//2 , n//2



result = matrix[x][y]

for i in range(t) :
    order = ori_order[i]

    if order == "F" :
        nx , ny = x + dxs[dir], y +dys[dir]
        if not in_range(nx,ny) :
            pass
        else :
            x, y = x  + dxs[dir] , y +dys[dir]
            result += matrix[x][y]
    
    elif order == "R" :
        dir = (dir +1) % 4
    
    else :
        dir = (dir + 3 ) % 4
    

print(result)