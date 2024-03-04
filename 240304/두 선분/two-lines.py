import sys

input = sys.stdin.readline


a,b,c,d = map(int,input().split())

count = 0

for i in range(a,b+1) :
    if c <= i <= d :
        count+=1
        break

if count != 0 :
    print('intersecting')

else :
    print('nonintersecting')