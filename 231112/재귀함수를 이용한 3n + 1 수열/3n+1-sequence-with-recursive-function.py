import sys

input  = sys.stdin.readline


N = int(input())


def sigma(N) :
    if N == 1 :
        return 0
    if N % 2 == 0 :
        return sigma(N//2) + 1
    else :
        return sigma(3*N +1) + 1



print(sigma(N))