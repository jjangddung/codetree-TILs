import sys

input = sys.stdin.readline


n = int(input())


arr = [list(map(int, input().split())) for _ in range(n)]

result_list = []


for i in range(n) :
    for j in range(1,n-1) :
        ori_arr = arr[i][j-1:j+2]
        result = sum(ori_arr)
        for p in range(n) :
            if p == i :
                for q in range(j+3,n-1) :
                    new_arr = arr[p][q-1:q+2]
                    new_result = result + sum(new_arr)
                    result_list.append(new_result)
            else :
                for q in range(1,n-1) :
                    new_arr = arr[p][q-1:q+2]     
                    new_result = result + sum(new_arr)
                    result_list.append(new_result)


print(max(result_list))