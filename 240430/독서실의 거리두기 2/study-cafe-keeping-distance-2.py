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

    for index in range(n) :
        new_table += str(num_list[index]) 
    
    new_string = new_table.split('1')
    arr = []
    for p in range(len(new_string)) :
        if len(new_string[p]) > 0 :
            arr.append(len(new_string[p]))
    value = min(arr)
    if value > min_value :
        min_value = value

print(min_value)