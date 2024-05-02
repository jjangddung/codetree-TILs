import sys

input = sys.stdin.readline


n = int(input())


matrix = [list(map(int, input().split())) for _ in range(n)]



maxi = 0

for i in range(n) :
    for j in range(n) :
        if i > n-3 or j > n-3 :
            continue
        
        new_mat = matrix[i:i+3][j:j+3]
        # print(new_mat)
        total_sum = 0
        for col in new_mat :
            total_sum += sum(col)
        maxi = max(total_sum , maxi)


print(maxi)