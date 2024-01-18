import sys

input = sys.stdin.readline

n = int(input())

x = 0
y = 0

for i in range(n) :

    i = list(map(str, input().split()))

    direction = i[0]
    count  = int(i[1])


    if direction == 'N' :
        y += count
    elif direction == 'E' :
        x += count
    elif direction == 'S' :
        y -=count
    else :
        x -=count


print(x,y)