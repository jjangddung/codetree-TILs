import sys

input = sys.stdin.readline


n, m = map(int ,input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m) :
    x,y = map(int, input().split())
    matrix[x-1][y-1] += 1
    matrix[y-1][x-1] += 1


maxi = 0

for j in range(n) :
    for p in range(n) :
        maxi = max(maxi,matrix[j][p])


print(maxi)