import sys

input =sys.stdin.readline

n = int(input())

lane = [0]* 101

for _ in range(n) :
    x_1,x_2 = map(int, input().split())

    for x in range(x_1,x_2+1) :
        lane[x] += 1


count = 0

for value in lane :
    if value == n :
        print('Yes')
        count +=1
        break

if count == 0 :
    print('No')