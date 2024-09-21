import sys


n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def nap(y) :
    if 0 < y and y < n-1 :
        return True



maxi = 0

for i in range(n) :
    for j in range(n) :
        if nap(j) :
            result = grid[i][j-1] + grid[i][j] +grid[i][j+1]
            maxi = max(result, maxi)


print(maxi)