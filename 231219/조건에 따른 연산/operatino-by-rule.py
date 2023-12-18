import sys

input = sys.stdin.readline


N = int(input())


cnt  = 0

k = N

while True :
    if k % 2 == 0 :
        k = k*3 + 1
    else :
        k = k *2 + 2
    cnt +=1
    if k >= 1000 :
        print(cnt)
        break