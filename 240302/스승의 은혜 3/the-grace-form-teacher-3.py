import sys


input = sys.stdin.readline


n,b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


matrix.sort()

result_list = []

for i in range(n) :
    sum_list = []

    for j in range(n) :
        
        if i == j :
            matrix[j][0] = matrix[j][0]//2
        ele = sum(matrix[j])
        sum_list.append(ele)

    result = 0
    # print(sum_list)

    b_copy =b
    
    for element in sum_list :
        if b_copy >= element :
            b_copy -= element
            result +=1
        else :
            pass
    result_list.append(result)

print(max(result_list))