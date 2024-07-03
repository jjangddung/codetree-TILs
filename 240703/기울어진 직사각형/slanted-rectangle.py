# 움직이는 횟수를 정하기 끝에  점들이  영역 밖으로 넘어가는지 확인하기

# >>> 첫번째 움직임  = 세번째 움직이
# >>> 2번째 움직임 = 4번째 움직임


import sys


input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y) :
    return 0 <=x < n and 0 <= y < n 


def point(x,y,first,second) :
    x,y 


dir_x = [-1,-1,1,1]
dir_y = [1,-1,-1,1]


maxi = 0

for x in range(n) :
    for y in range(n) :
        
        for fir  in range(1,n) :
            for sec in range(1,n) :
                total  = 0
                if not in_range(x+sec*dir_x[1],y+sec*dir_y[1]) :
                    continue
                
                p_x = x+fir*dir_x[0]
                p_y = y+fir*dir_y[0]

                if not in_range(p_x,p_y) :
                    continue

                if not in_range(p_x+sec*dir_x[1],p_y + sec*dir_y[1]) :
                    continue

                new_x, new_y = x, y
                for one in range(fir) :
                    new_x, new_y = new_x + dir_x[0] , new_y + dir_y[0]
                    total += matrix[new_x][new_y]
                
                for two in range(sec) :
                    new_x, new_y = new_x + dir_x[1] , new_y + dir_y[1]
                    total += matrix[new_x][new_y]

                for three in range(fir) :
                    new_x, new_y = new_x + dir_x[2] , new_y + dir_y[2]
                    total += matrix[new_x][new_y]
                
                for four in range(sec) :
                    new_x, new_y = new_x + dir_x[3] , new_y + dir_y[3]
                    total += matrix[new_x][new_y]
                
                maxi = max(total,maxi)


print(maxi)