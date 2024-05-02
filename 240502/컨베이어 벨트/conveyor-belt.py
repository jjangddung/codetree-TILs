import sys

input = sys.stdin.readline


n,t = map(int, input().split())


mat_1 = list(map(int, input().split()))
mat_2 = list(map(int, input().split()))

mat_3 = mat_1 + mat_2

length = len(mat_3)
for time in range(t) :
    temp = mat_3[length-1]
    i = length-1
    while i >- 0 :
        mat_3[i] = mat_3[i-1]
        i-=1
    mat_3[0] = temp

for i in range(length) :
    print(mat_3[i], end= " ")
    if i ==n-1 :
        print()