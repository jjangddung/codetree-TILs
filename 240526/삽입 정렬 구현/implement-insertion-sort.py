import sys

input = sys.stdin.readline


n = int(input())


matrix = list(map(int ,input().split()))



for i in range(n) :
    least = i
    for j in range(i+1, n) :
        if matrix[least] > matrix[j] :
            least = j
    
    if least != i :
        matrix[least] , matrix[i] = matrix[i] , matrix[least]


print(*matrix)