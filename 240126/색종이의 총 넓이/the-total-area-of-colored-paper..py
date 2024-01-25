import sys


input = sys.stdin.readline


n= int(input())


arr = [[0 for i in range(201)] for  j in range(201)]


for _ in range(n) :
    x_1, y_1 = map(int, input().split())

    for k in range(x_1+100, x_1+108) :
        for j in range(y_1+100, y_1+108) :
            arr[k][j] = 1



sum = 0

for k in arr :
    for j in k :
        sum += j


print(sum)