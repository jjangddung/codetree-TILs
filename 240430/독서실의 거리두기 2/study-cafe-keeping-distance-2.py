import sys

input = sys.stdin.readline


n = int(input())


string = input()
min_value = 0


for  i in range(n) :
    num_list = []
    new_table = ''


    for index in range(n) :
            num_list.append(int(string[index]))
    
    if num_list[i] == 1 :
        continue
    
    num_list[i] = 1

    one_index_list = []


    for index , num in enumerate(num_list) :
        if num == 1 :
            one_index_list.append(index)
    mini = 10000
    for s in range(1,len(one_index_list)) :
        value = one_index_list[s] - one_index_list[s-1]
        mini = min(value, mini)
    min_value = max(mini, min_value)
        


print(min_value)