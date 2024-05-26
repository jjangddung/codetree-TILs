import sys


input = sys.stdin.readline

n = int(input())


matrix = [list(map(int , input().split())) for _ in range(n)]


dxs  = [1,1,-1,-1] #왼아대 , 오아대 , 오위대 , 왼위대
dys  = [-1,1,1,-1]


maxi_sum = 0

def in_range(x,y) :
    return   0 <= x < n  and 0 <= y < n 

def equal(x,y,n_x,n_y) :
    return x == n_x and y == n_y

for r in range(n) :
    for c in range(n) :
        total_sum = 0 

        new_x , new_y =  r , c
        total_sum += matrix[new_x][new_y]
        count = 0
        for dx, dy in zip (dxs, dys) :
            count +=1
            while True :
                new_x , new_y =  new_x +dx , new_y +dy
                if not in_range(new_x,new_y) :
                    break
                if equal(r,c,new_x,new_y) :
                    # total_sum += matrix[new_x][new_y]
                    break 
                total_sum += matrix[new_x][new_y]

        if count != 4 :
            continue
        maxi_sum = max(total_sum, maxi_sum)

print(maxi_sum)