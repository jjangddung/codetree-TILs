import sys

input = sys.stdin.readline

start,end = map(int, input().split())
count = 0

for ele in range(start,end+1) :
    ele = str(ele)

    new_list = []
    for length in range(len(ele)) :
        new_list.append(int(ele[length]))
    
    # print(new_list)
    set_new_list = set(new_list)
    set_new_list = list(set_new_list)

    # print(set_new_list)

    if len(set_new_list) == 2:
        if new_list.count(set_new_list[0]) ==1 or new_list.count(set_new_list[1]) == 1:
            count +=1



print(count)