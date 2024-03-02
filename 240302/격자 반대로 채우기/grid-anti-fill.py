import sys

input = sys.stdin.readline

n = int(input())


matrix = [[0 for _ in range(n)] for _ in range(n)]

dxs = [-1,0,1,0]
dys = [0,-1,0,1]

matrix[n-1][n-1] = 1

i = n-1
dir = 0
count =1
while i >= 0 :
    
    if dir == 0 :
        for j in range(1,n+1) :
            matrix[n-j][i] =count
            count +=1
        dir = 1
    else :
        for j in range(0,n) :
            matrix[j][i] = count
            count +=1
        dir = 0
    i -=1

for  x in range(n) :
    for y in range(n) :
        print(matrix[x][y], end= " ")
    print()