import sys

input = sys.stdin.readline


n = int(input())

height_list = []

for _ in range(n) :
    height_list.append(int(input()))

low_height  = min(height_list)
high_height = max(height_list)

maxi = 0

for h in range(low_height,high_height+1) :

    new_height_list = []
    for j in range(n) :
        if height_list[j] - h > 0 :
            new_height = 1
        else :
            new_height = 0
        new_height_list.append(new_height)
    # print(new_height_list)
    real_list = []

    for num in range(n) :
        if num == 0 :
            real_list.append(new_height_list[num])
        if len(real_list) == 1 :
            if new_height_list[num] != real_list[0] :
                real_list.append(new_height_list[num])
        else :
            if new_height_list[num] != real_list[-1] :
                real_list.append(new_height_list[num])
    # print(real_list)
    maxi = max(sum(real_list),maxi)

print(maxi)