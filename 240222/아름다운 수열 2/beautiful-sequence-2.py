import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = list (map(int, input().split()))

b_arr = list(map(int, input().split()))


count = 0


for i in range(0,n-m+1) :
    new_arr = arr[i:i+m]
    b_copy_arr = b_arr.copy()
    new_check = []

    for i in new_arr :
        if i in b_copy_arr :
            new_check.append(i)
    
    if len(new_check) == m and sum(new_check) == sum(b_arr) :
        # print("같다!!")
        count +=1
        # print(new_check)
    # print(new_arr)

print(count)