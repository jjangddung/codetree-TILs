import sys

input = sys.stdin.readline


n,m = map(int, input().split())

arr =[[0 for i in  range(n)] for _ in  range(n)]





for i in range(m) :
    c,r = map(int, input().split())

    arr[c-1][r-1] = c*r


for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = " ")
    print()