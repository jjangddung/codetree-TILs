import sys

input = sys.stdin.readline

n = int(input())
matrix = list(map(int, input().split()))



sorted = False

while True :
    count = 0
    for i in range(n-1) :
        if matrix[i] > matrix[i+1] :
            tmp = matrix[i+1]
            matrix[i+1] = matrix[i]
            matrix[i] = tmp
            count +=1
    if count == 0 :
        break
    

print(*matrix)