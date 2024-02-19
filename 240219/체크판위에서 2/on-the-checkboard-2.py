import sys

input = sys.stdin.readline




r,c = map(int, input().split())

matrix = [list(map(str, input().split())) for _ in range(r)]




count  = 0

first_color = matrix[0][0]

last_color = matrix[r-1][c-1]

moving = []
for i in range(1,r-2) :
    for j in range(1,c-2) :
        if matrix[i][j] != first_color :
            ele = [i,j]
            moving.append(ele)
# print(ele)

for element in moving :
    x =  element[0]
    y =  element[1]

    for i in range(x+1,r-1) :
        for j in range(y+1,c-1):
            if matrix[i][j] == first_color :
                # print(x,y,i,j)
                count +=1


if last_color == first_color :
    print(0)

else :
    print(count)