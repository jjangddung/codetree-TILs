import sys

input = sys.stdin.readline


a,b,c = map(int, input().split())

N = int(a*b*c)

def plus(n) :
    if n <= 10 :
        return n 
    return plus(n//10) + n%10


print(plus(N))