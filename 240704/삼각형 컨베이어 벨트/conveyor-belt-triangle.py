import sys

input = sys.stdin.readline

n,t = map(int, input().split())


matrix = []

for _ in range(n) :
    new = list(map(int, input().split()))
    for p in range(n) :
        matrix.append(new[p])

move = t % (n*3)
first = matrix[n*3-move:] 
second = matrix[0:n*3-move]

final = first + second

mat_1 = final[0:n]
mat_2 = final[n:2*n]
mat_3 =  final[2*n:]
print(*mat_1)
print(*mat_2)
print(*mat_3)