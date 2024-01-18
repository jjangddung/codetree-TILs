import sys


input= sys.stdin.readline



n,m = map(int, input().split())

arr =[[0 for i in range(n)] for _ in range(n)]

cnt = 1;


for i in range(m) :
    c,r = map(int, input().split())

    arr[c-1][r-1] = cnt

    cnt+=1


for list in arr :
    for j in  range (n) :
        print(list[j], end= " ")
    print()