import sys

input = sys.stdin.readline


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

# print(matrix)

def make_square(x,y) :
    square = [[0 for _ in range(3)] for _ in range(3)]
    # print(square)

    for p in range(0,3) :
        for q in range(0,3) :
            square[p][q] = matrix[x-1+p][y-1+q]
    
    # print(square)
    
    total_sum = 0

    for element in square :
        for ele in element :
            total_sum += ele
    
    # print(total_sum)
    return total_sum

maxi = 0

for x in range(1,n-1) :
    for y in range(1,n-1) :
        result = make_square(x,y)
        maxi = max(result,maxi)


print(maxi)