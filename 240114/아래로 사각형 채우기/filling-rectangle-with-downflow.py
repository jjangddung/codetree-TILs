import sys

input = sys.stdin.readline


n = int(input())

cnt = 5

list_2 = []
for i in range(1,n+1) :
    list_1 = []
    for j in range(n) :
        list_1.append(i+cnt*j)
    list_2.append(list_1)


for i in range(n) :
    for j in range(n) :
        print(list_2[i][j], end= " ")
    print()