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
    new_list = set(new_list)
    if len(new_list) == 2 :
        count +=1

print(count)