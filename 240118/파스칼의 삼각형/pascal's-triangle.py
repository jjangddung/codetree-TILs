import sys


input = sys.stdin.readline


n = int(input())


arr= [[1 for i in range(j)]for j in range(1,n+1)]



for i in range(2,n) :
    for j in range(1,i) :
        arr[i][j] = arr[i-1][j-1] +arr[i-1][j]



for sub_list in arr :
    for j in sub_list :
        print(j, end= " ")
    print()