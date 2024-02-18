import sys

input = sys.stdin.readline


n = int(input())

matrix = [list(map(int, input().split()))for _ in range(n)]

max_result = 0


for row in matrix :
    for i in range(n-2) :
        sum = row[i] + row[i+1] + row[i+2]
        max_result = max(max_result,sum)


print(max_result)