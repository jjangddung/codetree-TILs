import sys

input = sys.stdin.readline



a,b = map(int, input().split())

cnt = 0 
while a <= b:
    if 1920 % a == 0 and 2880 % a == 0 :
        print(1)
        break
    a=a+1

if a == b+1 :
    print(0)