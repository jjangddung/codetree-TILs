import sys

n = int(input())


dys,dxs = [-1,0,1,0],[0,1,0,-1]

x,y = 0,0
for _ in range(n) :
    direct, num = map(str, input().split())
    num = int(num)


    if direct == 'N' :
        x,y = x + num*dxs[2] , y + num*dys[2]
    
    elif direct == 'E' :
        x,y = x + num*dxs[1] , y + num*dys[1]
    
    elif direct == 'S' :
        x,y = x + num*dxs[0] , y + num*dys[0]
    
    elif direct == 'W' :
        x,y = x + num*dxs[3] , y + num*dys[3]


print(x,y)