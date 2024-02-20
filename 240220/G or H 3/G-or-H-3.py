import sys

n, k = map(int, input().split())


arr = [0] * 10001

# print(arr)

for i in range(n) :
    n_list = list(map(str, input().split()))

    index = int(n_list[0])
    
    if n_list[1] == "G" :
        arr[index] = 1
    
    else :
        arr[index] = 2

max_val = 0

for i in range(1,10002-k) :
    new_arr = arr[i:i+k+1]
    new_val = sum(new_arr)

    max_val = max(max_val, new_val)


print(max_val)