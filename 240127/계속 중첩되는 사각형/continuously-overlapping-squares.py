import sys


input = sys.stdin.readline


n = int(input())


arr =[[0 for _ in range(201)]for p in range(201)]



for i in range(n) :
    x_1, y_1, x_2,y_2 = map(int , input().split())

    for j in range(x_1+100, x_2 + 100) :
        for k in range(y_1+100 , y_2+ 100) :
            if i % 2 == 0 :
                arr[j][k] = 2
            else :
                arr[j][k] = 1
    



sum = 0

for i in  arr :
    for j in i :
        if j  == 1 :
            sum +=1


print(sum)