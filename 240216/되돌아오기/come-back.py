import sys


input = sys.stdin.readline



n = int(input())


arr = [list(map(str, input().split())) for _ in range(n)]

x, y  = 0, 0

def checking(result) :
    if result == "N" :
        return 0
    elif result == "E" :
        return 1
    elif result == "S" :
        return 2
    else :
        return 3
    

dxs = [0,1,0,-1]
dys = [1,0,-1,0]


time = 0
cnt = 0
for p in arr :
    direct = p[0]
    dis = int(p[1])

    direct = checking(direct)

    for i in range(dis) :
        x, y = x + dxs[direct] , y + dys[direct]
        # print(x,y)
        time +=1

        if x == 0 and y == 0 :
            print(time)
            cnt = 1
            break
    if cnt == 1:
        break


if cnt == 0 :
    print(-1)