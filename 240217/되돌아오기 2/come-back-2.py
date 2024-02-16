import sys

input = sys.stdin.readline

global x
global y
global dir

arr = input()


dxs = [-1,0,1,0]
dys = [0,1,0,-1]

x,y = 0, 0 # 초기좌표




dir = 0
t = 0
def checking_dir(string) :
    global x
    global y
    global dir

    
    if string == "R" :

        dir = (dir+1)% 4

    elif string == "F" :

        x,y = x + dxs[dir] , y + dys[dir]
    else :

        dir = (dir +3) % 4

        


for i in range(len(arr)) :
    checking_dir(arr[i])

    t += 1
    if x == 0 and y == 0 :
        print(t)
        break
    
    if i == len(arr) -1 :
        print(-1)