import sys


input = sys.stdin.readline
n,m = map(int, input().split())
t  = n*m

arr = [[0 for i in range(m)] for _ in range(n)]



dxs = [-1,0,1,0] # 0,1,2,3 >>> 위 오 아 왼
dys = [0,1,0,-1]

first_dir =  1


def checking (x,y,n,m) :
    if 0 <= x < n and 0 <= y < m :
        return True
    
    else :
        return False


x, y = 0 , 0
start = 2
arr[0][0] = 1
# print(t)

for i in range(10002) :
    
    if first_dir == 0 : # 위로
        x , y = x + dxs[first_dir] , y + dys[first_dir]

        if checking(x,y,n,m) :

            if arr[x][y] != 0 :
                x +=1
                first_dir = 1
                
            else :
                arr[x][y] = start
                start +=1
            # print(arr[x][y])

        else :
            x += 1
            first_dir = 1


    
    elif first_dir == 1 : # 오른쪽
        x , y = x + dxs[first_dir] , y + dys[first_dir]

        if checking(x,y,n,m) :

            if arr[x][y] != 0 :
                y -= 1
                first_dir = 2
            else :
                arr[x][y] = start
                start +=1
        
        else :
            y -= 1
            first_dir = 2


        
    
    elif first_dir == 2 : #아래로
        x , y = x + dxs[first_dir] , y + dys[first_dir]

        if checking(x,y,n,m) :
            if arr[x][y] != 0 :
                x -=1
                first_dir = 3

            else:
                arr[x][y] = start
                start +=1

        else :
            x -= 1
            first_dir = 3

    
    elif first_dir == 3 : #왼쪽으로
        x , y = x + dxs[first_dir] , y + dys[first_dir]

        if checking(x,y,n,m) :
            if arr[x][y] != 0 :
                y +=1
                first_dir = 0
            else :
                arr[x][y] = start
                start +=1

        else :
            y += 1
            first_dir = 0
    


for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = " ")
    print()