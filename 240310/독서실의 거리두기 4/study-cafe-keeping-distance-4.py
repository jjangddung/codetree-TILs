import sys

input = sys.stdin.readline


n = int(input())

seat = input()
seat_list = []

for i in range(n) :
    seat_list.append(int(seat[i]))


maxi = 0


for i in range(n) :
    for j in range(n) :
        if seat_list[i] == 1 or seat_list[j] == 1 :
            continue
        seat_copy = []
        for p in range(n) :
            seat_copy.append(seat_list[p])
        seat_copy[i] = 1
        seat_copy[j] = 1

        seat_index = []
        for num, element in enumerate(seat_copy) :
            if element == 1 :
                seat_index.append(num)
        length  = len(seat_index)

        distance_list = []

        for short in range(1,length) :
            dis = seat_index[short] - seat_index[short-1]
            distance_list.append(dis)
        result = min(distance_list)
        maxi = max(maxi,result)


print(maxi)