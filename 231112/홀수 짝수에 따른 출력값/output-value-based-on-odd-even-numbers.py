import sys

input = sys.stdin.readline


N = int(input())

def printing(N) :
    if N <= 2 :
        return N

    return printing(N-2) + N


print(printing(N))