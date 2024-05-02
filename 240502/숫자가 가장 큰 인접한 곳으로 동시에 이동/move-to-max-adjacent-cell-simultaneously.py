import sys

input = sys.stdin.readline


n,m, t=  map(int, input().split())


count_matrix = [[0]*n  for _  in range(n)]

matrix = [list(map(int, input().split())) for _ in range(n)]
rc_list= [list(map(int, input().split())) for _ in range(m)]


dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y) :
    return  0<= x < n and 0 <= y < n 


real_list = []

for xy in rc_list :
    real_list.append([xy[0]-1,xy[1]-1])

# print(real_list)

for _ in range(t) :
    new_count_matrix = [[0]*n  for _  in range(n)]
    new_list = []


    for xy in real_list :
        curr_x , curr_y = xy[0] ,xy[1]
        maxi = 0
        maxi_x , maxi_y = curr_x ,curr_y

        for dx,dy in zip (dxs,dys) :
            next_x , next_y = curr_x +dx , curr_y +dy
            if in_range(next_x,next_y) and matrix[next_x][next_y] > maxi:
                maxi = matrix[next_x][next_y]
                maxi_x = next_x
                maxi_y = next_y
        
        new_count_matrix[maxi_x][maxi_y] += 1
    # print(new_count_matrix)
    for r in range(n) :
        for c in range(n) :
            if new_count_matrix[r][c] > 1 :
                new_count_matrix[r][c] == 0
            elif new_count_matrix[r][c] == 1 :
                new_list.append([r,c])
    real_list = new_list


print(len(real_list))