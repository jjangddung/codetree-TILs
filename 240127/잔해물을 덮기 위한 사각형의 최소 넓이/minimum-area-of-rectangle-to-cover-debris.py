import sys


input = sys.stdin.readline

x_1,y_1,x_2,y_2 = map(int, input().split())


arr = [[0 for _ in range(2001)] for i in range(2001)]


for i in range(x_1+1000,x_2+1000) :
    for j in range(y_1+1000,y_2+1000) :
        arr[i][j] = 1
    

x_3, y_3, x_4, y_4 = map(int, input().split())

for i in range(x_3+1000,x_4+1000) :
    for j in range(y_3+1000,y_4+1000) :
        arr[i][j] = 0

x_list = []
y_list = []

for i in range(x_1+1000, x_2+1000) :
    cnt = 0

    for j in range(y_1+1000,y_2+1000) :
        if arr[i][j] == 1 :
            cnt += 1
    if cnt != 0 :
        x_list.append(i)

    
for j in range(y_1+1000,y_2+1000) :
    cnt = 0

    for i in range(x_1+1000, x_2 +1000) :
        if arr[i][j] == 1:
            cnt +=1
    if cnt != 0 :
        y_list.append(j)

    

x_length  = max(x_list) - min(x_list) +1
y_length = max(y_list) - min(y_list) +1

print(x_length*y_length)