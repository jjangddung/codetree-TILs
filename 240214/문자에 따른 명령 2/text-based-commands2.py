import sys

input = sys.stdin.readline


order = input()


length = len(order)

initial_x = [0,0,0,0] # 북 > 동 > 남  > 서
initial_y = [0,0,0,0] # 북 > 동 > 남 > 서


index = 0

for i in order :
    if i  == "R" :
        index += 1
        index = index % 4

    elif i == "L" :
        index += 3
        index = index % 4
    
    elif i == "F" :
        if index == 0 :
            initial_y[index] +=1
        elif index == 1 :
            initial_x[index] += 1
        elif index == 2 :
            initial_y[index] -=1
        elif index == 3 :
            initial_x[index] -= 1



print(sum(initial_x), sum(initial_y))