import sys


input = sys.stdin.readline




n,m = map(int, input().split())


arr = [[0 for i in range(n)]for j in range(n)]


for i in range(m) :
    k,l = map(int, input().split())

    for j in range(n) :
        arr[k-1][l-1] = 1


for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end= " ")
    print()