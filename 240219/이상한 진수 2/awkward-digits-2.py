import sys

input = sys.stdin.readline


arr = input()
length  = len(arr)

num_list = []

for i in arr :
    num_list.append(i)

# num_list = num_list[::-1]

# print(num_list)
count = 0
for i in range(1, length) :
    if num_list[i] == "0" :
        count +=1
        num_list[i] =  "1"
        break

if count == 0 :
    for i in range(length) :
        if num_list[length-1-i] == "1" :
            num_list[length-1-i] = "0"
            break


# print(num_list)
result = 0
for i in range(length) :
    ori = int(num_list[i])
    multi = 2 **(length-1-i)
    ori *=multi
    result += ori

print(result)