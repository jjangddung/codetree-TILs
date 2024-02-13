import sys


input = sys.stdin.readline



def in_range(x,y,num) :
    if 0 <= x < num and 0 <= y < num :
        return True






n = int(input())



arr = [list(map(int, input().split())) for  _ in range(n)]


dxs, dys =  [0,1,0,-1], [1,0,-1,0] # 북 >>> 동 >>> 남 >>> 서 

coordinate = []

for i in range(n) :
    for j in range(n) :
        k = [i,j]
        coordinate.append(k)


count  = 0

for coor in coordinate :
    x = coor[0]
    y = coor[1]
    cnt = 0

    for dir_num in range(4) :
        
        nx , ny = x + dxs[dir_num] , y + dys[dir_num]
        if in_range(nx,ny,n) and arr[nx][ny] == 1 :
            
            cnt +=1
    if cnt >= 3 :
        count +=1 


print(count)