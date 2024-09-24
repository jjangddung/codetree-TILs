import sys
import copy





n = int(input())

lst = list(map(int, input().split()))



value = 0

new_lst = copy.deepcopy(lst)

# print(new_lst)
while len(new_lst) > 1 :
    new_lst = sorted(new_lst)
    # print(new_lst)
    value = new_lst[0] + new_lst[1]
    new_lst = [value] +new_lst[2:]
    # print(new_lst)


print(value + new_lst[0])