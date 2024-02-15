import sys

input = sys.stdin.readline



n, t = map(int, input().split())


r,c,d = map(str, input().split())

x,y = int(r)-1 , int(c)-1



dxs = [-1,0,1,0] # x = col , y = row
dxy = [0,1,0,-1]


def checking(x,y,n) :
    if 0 <= x < n and 0 <= y < n :
        return True

    else :
        return False



first_dir = d 


time = 0

while time < t :

    if first_dir == "U" :
        x, y  = x+ dxs[0] , y+ dxy[0]

        if  checking(x,y,n) :
            time+=1

        else :
            first_dir = "D"
            x +=1
            time +=1

    
    elif first_dir == "R" :

        x, y  = x+ dxs[1] , y+ dxy[1]

        if checking(x,y,n) :
            time+=1
        
        else :
            first_dir = "L"
            y -= 1
            time +=1


    
    elif first_dir == "D" :

        x, y  = x+ dxs[2] , y+ dxy[2]

        if checking(x,y,n) :
            time+=1
        else :
            first_dir = "U"
            x -=1
            time +=1
    
    else :

        x, y  = x+ dxs[3] , y+ dxy[3]

        if checking(x,y,n) :
            time += 1
        
        else :
            first_dir = "R"
            y +=1
            time +=1


print(x+1, y+1)