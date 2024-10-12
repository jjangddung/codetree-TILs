import sys


dxs, dys = [0,1,0,-1],[1,0,-1,0]



order = str(input())
length = len(order)

x,y,direct = 0,0,0

for  i in range(length) :
    if order[i] == 'L' :
        direct -=1
        if direct < 0 :
            direct == 3
    
    elif order[i] == 'R' :
        direct +=1

        if direct > 3 :
            direct == 0
    
    else :
        x,y = x+ dxs[direct] , y +dys[direct]


print(x,y)