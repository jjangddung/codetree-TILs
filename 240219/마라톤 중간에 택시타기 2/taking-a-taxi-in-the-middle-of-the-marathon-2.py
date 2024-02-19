import sys

input = sys.stdin.readline


n = int(input())

check_point = [list(map(int, input().split())) for _ in range(n)]



distance_list = []

first_x , first_y = check_point[0][0] , check_point[0][1]


for i in range(1,n-1) :
    new_list = []
    for ele in check_point :
        new_list.append(ele)
    distance = 0
    new_list.pop(i)
    # print(new_list)
    # print(check_point)

    for i in range(1,n-1) :
        distance += abs(new_list[i][0]- new_list[i-1][0]) + abs(new_list[i][1]- new_list[i-1][1])
    distance_list.append(distance)

# print(check_point)
print(min(distance_list))