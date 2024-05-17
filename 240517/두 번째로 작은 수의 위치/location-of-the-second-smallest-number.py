import sys

input = sys.stdin.readline



n = int(input())

matrix = list(map(int, input().split()))

new_matrix = matrix.copy()

new_matrix = set(new_matrix)
new_matrix = list(new_matrix)

new_matrix.sort()
# print(matrix)

if len(new_matrix) >= 2:

    element = new_matrix[1]

    if  matrix.count(element) != 1 :
        print(-1)

    else :
        print(matrix.index(element)+1)

else :
    print(-1)