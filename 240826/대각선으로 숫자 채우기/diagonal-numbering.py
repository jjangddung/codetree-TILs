import sys

n,m = map(int, input().split())




grid = [[0]*m for _ in range(n)]

#대각선의 개수를 알면 되는 문제








num= 1
for total in range(n+m-1) :
    for j in range(total+1) :
        try :
            grid[j][total-j] = num
            num +=1
        except :
            pass
for g in grid :
    print(*g)