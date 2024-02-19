import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input())for _ in range(n)]

# print(arr)

distance_list = []


for i in range(n) :
    distance = 0
    for j in range(n) :
        if i <= j :
            distance += arr[j] * (j-i)
        else :
            distance += arr[j] * (n-i+j)
    distance_list.append(distance)

print(min(distance_list))