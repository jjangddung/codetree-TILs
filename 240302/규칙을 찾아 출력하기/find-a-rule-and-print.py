import sys

input = sys.stdin.readline

n = int(input())


for i in range(n) :
    if i == 0 :
        print('* '*n)
    else :
        for j in range(i) :
            print('*', end= " ")
        for p in range(n-i-1) :
            print(" ", end= " ")
        print("*")