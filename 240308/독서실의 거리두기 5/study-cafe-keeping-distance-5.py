import sys

input = sys.stdin.readline


n = int(input())



seat = input()

arr = []
for i in range(n) :
    arr.append(seat[i])


real_maxi = 0

for i in range(n) :
    arr_copy= []
    for j in range(n) :
        arr_copy.append(int(arr[j]))
    if arr_copy[i] != 1:
    
        arr_copy[i] = 1
        # print(arr_copy)
        # print("arr_copy:", arr_copy)
        check_list = []
        for t in range(n) :
            if arr_copy[t] == 1:
                check_list.append(t)

        # print(check_list)
        new_list = []
        for p in range(len(check_list)-1) :
            k = check_list[p+1] -check_list[p]
            new_list.append(k)
        result = 0
        try:
            result = min(new_list)
        except :
            pass
            # print(check_list)

        real_maxi = max(real_maxi,result)



print(real_maxi)