import sys
import copy


input = sys.stdin.readline


n = int(input())

lst = list(map(int, input().split()))



value = 0
result = 0
new_lst = copy.deepcopy(lst)

# print(new_lst)
while len(new_lst) > 1 :
    new_lst = sorted(new_lst)
    # print(new_lst)
    value = new_lst[0] + new_lst[1]
    result  += value
    new_lst = [value] +new_lst[2:]
    # print(new_lst)



if len(new_lst) == 1 :
    print(result)