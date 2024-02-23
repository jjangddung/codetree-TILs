import sys

input = sys.stdin.readline


n = int(input())


arr = [0] * 101

for i in range(n) :
    index, alphabet = map(str, input().split())
    index = int(index)
    if alphabet == "G" :

        arr[index] = 2
    else :
        arr[index] = 1


max_i = 0

for i in range(1,102) :
    for j in range(101-i+1) :
        new_arr = arr[j:j+i]
        if new_arr[0] != 0 and new_arr[-1] != 0 :
            if new_arr.count(1) == new_arr.count(2) and new_arr.count(1) != 0 :
                max_i = max(max_i,i-1)
    

print(max_i)