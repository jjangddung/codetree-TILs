import sys

input = sys.stdin.readline


n,k = map(int, input().split())



arr =[int(input()) for _ in range(n)]

set_arr = set(arr)

maxi = 0

for ele in set_arr :
    new_list = []
    for num in arr :
        if 0<= (num-ele) <= k :
            new_list.append(num)
    length = len(new_list)
    maxi = max(maxi,length)
    # print(new_list)

print(maxi)