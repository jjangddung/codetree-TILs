import sys


input = sys.stdin.readline

n,k = map(int, input().split())

arr = list(map(int, input().split()))

set_arr = set(arr)
set_arr = list(set_arr)
set_arr.sort()



def check_possible(max_val) :
    availale_indices = []

    for i, elem in enumerate(arr) :
        if elem <= max_val :
            availale_indices.append(i)
    
    arr_size = len(availale_indices)
    for i in range(1,arr_size) :
        dist = availale_indices[i] -availale_indices[i-1] 
        if dist > k :
            return False
    
    # print(availale_indices)
    count =  0

    for p in availale_indices : 
        if p ==  0 or p == n-1 :
            count +=1
    if count == 2 :
        # print(availale_indices)
        return True
    else :
        return False

minmax = 100000

for a in set_arr:
    if check_possible(a):
        minmax = min(minmax, a)

print(minmax)