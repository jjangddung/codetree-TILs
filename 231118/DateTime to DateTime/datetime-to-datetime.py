import sys

input = sys.stdin.readline

d,h,m = map(int, input().split())

num_1 = (11+24*10)*60 + 11
num_2 = (h+(d-1)*24)*60 + m

if num_1 < num_2 :
    print(num_2-num_1)

else :
    print(-1)