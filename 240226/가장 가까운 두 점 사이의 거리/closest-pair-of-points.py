import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]


min_dis = 10000000000




for i in range(n-1) :
    for j in range(i+1,n) :
        x_1, y_1 = arr[i][0] , arr[i][1]

        x_2, y_2 = arr[j][0] , arr[j][1]

        dis = (x_1-x_2)*(x_1-x_2) + (y_1-y_2)*(y_1-y_2)

        min_dis = min(min_dis,dis)


print(min_dis)