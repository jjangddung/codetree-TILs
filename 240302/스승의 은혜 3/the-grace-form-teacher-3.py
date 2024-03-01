import sys


input = sys.stdin.readline


n,b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


matrix.sort()

maximum = 0

for i in range(n) :
    sum_list = []
    matrix_copy = matrix.copy()

    for j in range(n) :
        
        if i == j :
            matrix_copy[j][0] = matrix_copy[j][0]//2
        ele = sum(matrix_copy[j])
        sum_list.append(ele)
    sum_list.sort()
    result = 0
    # print(sum_list)

    # print(b_copy)
    assume = 0

    for element in sum_list :
        assume += element
        if assume <= b :
            result +=1
            
        
    maximum = max(maximum,result)

print(maximum)