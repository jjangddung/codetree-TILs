import sys
n, m = map(int, input().split())
grid = list(map(int, input().split()))
num_lst = list(map(int, input().split()))

for num in num_lst:
    try :
        print(grid.index(num)+1)
    except :
        print(-1)