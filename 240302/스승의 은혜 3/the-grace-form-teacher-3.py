import sys


input = sys.stdin.readline


n,b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


# matrix.sort()

maximum = 0

for i in range(n) :
    sum_list = []
    matrix_copy = []
    for w in range(n) :
        matrix_copy.append(matrix[w])

    # / print(sum_list)
    # print(matrix_copy)

    for j in range(n) :
        
        if i == j :
            ele = matrix_copy[j][0]//2 + matrix_copy[j][1]
        else :
            ele = matrix_copy[j][0] + matrix_copy[j][1]
        # print(f'j:{j}')
        sum_list.append(ele)
    # print(matrix_copy)
    sum_list.sort()
    result = 0
    # print(sum_list)

    # print(b_copy)
    assume = 0

    for p in range(n) :
        assume += sum_list[p]
        if assume <= b :
            result +=1
        
        else :
            break

        
    maximum = max(maximum,result)

print(maximum)