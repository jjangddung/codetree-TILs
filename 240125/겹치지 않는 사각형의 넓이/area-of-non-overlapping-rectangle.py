import sys

input = sys.stdin.readline




sum = 0

arr = [[0 for _ in range(2001)] for i in range(2001)]
for p in range(3) :
    x_1,y_1,x_2,y_2 = map(int, input().split())
    for i in range(x_1+1000,x_2+1000) :
        for j in range(y_1+1000,y_2+1000) :

            if p < 2 :
                arr[i][j] = 1
            
            else :
                if  arr[i][j] != 0 :
                    arr[i][j] = 0


for l in arr :
    for j in l :
        sum += j


print(sum)