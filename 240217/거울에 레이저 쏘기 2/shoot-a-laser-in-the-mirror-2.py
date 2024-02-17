import sys

input = sys.stdin.readline

global dir

dxs = [1,0,-1,0] #  down, left , up, right
dys = [0,-1,0,+1]


n = int(input())

mirror = [input().strip() for _ in range(n)]


mirror_matrix = [[0 for _ in range(n)] for i in range(n)]


for  i in range(n) :
    for j in range(n) :
        k = 0
        if mirror[i][j] == '/' :
            k = 0
        else :
            k = 1
        
        mirror_matrix[i][j] = k


# print(mirror_matrix)

ori_dir = int(input())
dir = 0

dir_matrix = []

if ori_dir <= n :
    x = 0
    y = ori_dir - 1
    dir = 0

elif ori_dir <= 2*n :
    x = ori_dir - (n+1)
    y = n-1
    dir = 1

elif ori_dir <= 3*n :
    x = n -1
    y = 3*n - ori_dir
    dir = 2
else :
    x = 4*n - ori_dir
    y = 0
    dir = 3


count = 0

def turn_right() :
    global dir
    dir = (dir +1) % 4

def turn_left() :
    global dir
    dir = (dir+3) % 4



while 0 <= x < n and 0 <= y < n :

    if dir == 0 and mirror_matrix[x][y] == 0 :
        turn_right()
        # x, y = x + dxs[dir] , y + dys[dir]
    
    elif dir == 0 and mirror_matrix[x][y] == 1 :
        turn_left()

    elif dir == 1 and mirror_matrix[x][y] == 0 :
        turn_left()
    
    elif dir == 1 and mirror_matrix[x][y] == 1:
        turn_right()
    
    elif dir == 2 and mirror_matrix[x][y] == 0 :
        turn_right()

    elif dir == 2 and mirror_matrix[x][y] == 1:
        turn_left()
    
    elif dir == 3 and mirror_matrix[x][y] == 0 :
        turn_left()
    
    else :
        turn_right()
    
    x,y = x + dxs[dir] , y + dys[dir]
    count +=1

print(count)