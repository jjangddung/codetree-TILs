import sys


input = sys.stdin.readline

n = int(input())

count = 0

arr = list(map(int, input().split()))

for i in range(1,n+1) :
    for j in range(n-i+1) :

        new_arr = (arr[j:j+i])
        # if arr_list.count(new_arr) == 0 :
            # arr_list.append(new_arr)
            # avg = sum(new_arr)/i
            # print(avg)
            # for p in arr :
                # if avg == p :
                    # count +=1
                    # print("통과",avg)
                    # break
        # else :
            # pass
        avg = sum(new_arr)/i
        for p in new_arr :
            if avg == p :
                count +=1
                break
        

        

print(count)