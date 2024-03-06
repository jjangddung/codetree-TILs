import sys

input = sys.stdin.readline

n = int(input())

arr = str(input())

for i in range(1,n) :
    new_list = []
    for j in range(n) :
        new_ele = arr[j:j+i]
        new_list.append(new_ele)
    set_new_list = set(new_list)
    if len(set_new_list) == len(new_list) :
        print(i)
        break