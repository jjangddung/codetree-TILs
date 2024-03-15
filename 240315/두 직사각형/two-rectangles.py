import sys

input = sys.stdin.readline


fisrt_square = list(map(int, input().split()))
second_square = list(map(int, input().split()))


matrix = [[0 for _ in range(101)] for i in range(101)]



for x in range(fisrt_square[0],fisrt_square[2]+1) :
    for y in range(fisrt_square[1],fisrt_square[3]+1):
        matrix[x][y] += 1

count = 0
for x in range(second_square[0],second_square[2]+1) :
    
    for y in range(second_square[1],second_square[3]+1):
        if matrix[x][y] == 1 :
            # print(x,y)
            print("overlapping") 
            count +=1
            break
        else :
            matrix[x][y] += 1
    if count != 0 :
        break

if count == 0 :
    print('nonoverlapping')