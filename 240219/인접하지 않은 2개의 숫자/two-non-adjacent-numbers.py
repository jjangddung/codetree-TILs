import sys

input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))

length = len(arr)

result_list = []

for i in range(length-1) :
    for j in range(i+2, length) :
        result = arr[i] + arr[j]
        result_list.append(result)



print(max(result_list))