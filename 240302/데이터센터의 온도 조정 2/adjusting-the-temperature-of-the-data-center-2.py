import sys

input = sys.stdin.readline

n,c,g,h = map(int, input().split())

temp = [list(map(int, input().split())) for _ in range(n)]

low_temp = 0
high_temp = 1000
maxi = 0

for temper in range(high_temp+1) :
    work = 0
    for ele in temp :
        if temper < ele[0] :
            work +=c
        elif temper > ele[1] :
            work +=h
        else :
            work +=g
    maxi = max(maxi,work)


print(maxi)