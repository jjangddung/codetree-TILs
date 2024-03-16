import sys

input =sys.stdin.readline

n = int(input())


gugu = [list(map(int , input().split())) for _ in range(n)]

gugu_list= [2] * 11


count  = 0

for i in range(n) :
    num_1=gugu[i][0]
    position = gugu[i][1]
    if gugu_list[num_1] == 2:
        gugu_list[num_1] = position
    
    else :
        if gugu_list[num_1] != position :
            count +=1
            gugu_list[num_1] = position

print(count)