import sys

input = sys.stdin.readline


n,r,c = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]




r,c = r-1, c-1
curr_x, curr_y = r , c
print(matrix[curr_x][curr_y], end= " ")

def in_range(x,y) :
    return 0 <= x < n  and 0 <= y < n 


dxs = [-1,1,0,0]
dys = [0,0,-1,1]
while True:
    count = 0
    for dx, dy in zip(dxs,dys) :
        next_x, next_y = curr_x + dx, curr_y + dy
        if in_range(next_x,next_y) and matrix[next_x][next_y] > matrix[curr_x][curr_y] :
            curr_x, curr_y = next_x, next_y 
            print(matrix[curr_x][curr_y], end= " ")
            count +=1
            break
    if count == 0 :
        break