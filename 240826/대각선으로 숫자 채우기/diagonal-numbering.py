import sys

n,m = map(int, input().split())




grid = [[0]*m for _ in range(n)]



if m == 1 :
    for i in range(1,n+1) :
        print(i)

num= 1
for total in range(2*m) :
    for j in range(total+1) :
        try :
            grid[j][total-j] = num
            num +=1
        except :
            pass

for g in grid :
    print(*g)