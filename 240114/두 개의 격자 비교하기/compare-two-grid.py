import sys

input = sys.stdin.readline

n,m = map(int,input().split())


arr_1 = [list(map(int, input().split())) for _ in range(n)]

arr_2 = [list(map(int, input().split())) for _ in range(n)]

# print(arr_1)
# print(arr_2)



arr_3 = [[1 for j in range(m)] for i in range(n)]

for i in range(n) :
    for j in range(m) :
        if arr_1[i][j] == arr_2[i][j] :
    
            arr_3[i][j] = 0

for i in range(n) :
    for j in range(m) :
        print(arr_3[i][j], end= " ")
    print()