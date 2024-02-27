import sys

input = sys.stdin.readline


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

rectangular = []

for i in range(n) :
    new_x_arr = []
    new_y_arr = []

    for j in range(n) :
        if j == i :
            continue
        x, y = arr[j]
        new_x_arr.append(x)
        new_y_arr.append(y)
    max_x, max_y = max(new_x_arr) , max(new_y_arr)
    min_x, min_y = min(new_x_arr) , min(new_y_arr)
    rec = (max_x-min_x)*(max_y-min_y)
    rectangular.append(rec)

print(min(rectangular))