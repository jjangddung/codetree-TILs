#끝 점 좌표 4개를 임의로 정하기


import sys

input = sys.stdin.readline


n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def change_grid(value,n,m) :
    new_value = [value//m,value % m]

    return new_value

def width_height(value_1,value_2) :
    width = value_2[0] - value_1[0] +1
    height = value_2[1] - value_1[1] +1

    return [width,height]

maxi  = 0



for p_max in range(n*m) :
    for p_min in range(n*m):
        for q_max in range(n*m) :
            if p_max == q_max or p_min == q_max :
                continue
            for q_min in range(n*m) :
                if p_max == q_min or p_min == q_min :
                    continue

                if p_min < p_max :
                    continue
                if q_min < q_max :
                    continue
                
                p_left_grid = change_grid(p_max,n,m)
                p_right_grid = change_grid(p_min,n,m)
                q_left_grid = change_grid(q_max,n,m)
                q_right_grid = change_grid(q_min,n,m)

                total  = 0 
                value_1 = width_height(p_left_grid,p_right_grid)
                value_2 = width_height(q_left_grid,q_right_grid)
                new_matrix = [[0]*m for _ in range(n)]

                for x in range(p_left_grid[0],p_left_grid[0]+value_1[0]+1) :
                    for y in range(p_left_grid[1],p_left_grid[1]+value_1[1]+1) :
                        new_matrix[x][y] += 1
                for x in range(q_left_grid[0],q_left_grid[0]+value_2[0]+1) :
                    for y in range(q_left_grid[1],q_left_grid[1]+value_2[1]+1) :
                        new_matrix[x][y] +=1
                
                for x, y in zip(range(n), range(m)) :
                        if new_matrix[x][y] != 0 :
                            if new_matrix[x][y] > 1 :
                                total = 0
                                break
                            total += matrix[x][y]
                maxi = max(total, maxi)

print(maxi)