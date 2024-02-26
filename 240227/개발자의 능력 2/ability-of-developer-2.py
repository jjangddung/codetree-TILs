import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))


arr.sort()


matrix = [[0,5],[1,4],[2,3]]

result_list = []

for ele in matrix :
    x, y = ele[0] , ele[1]
    result = arr[x] + arr[y]
    result_list.append(result)


print(max(result_list)-min(result_list))