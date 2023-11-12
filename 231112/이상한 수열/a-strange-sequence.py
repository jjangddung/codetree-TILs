import sys

input  = sys.stdin.readline


N = int(input())


def func(N) :
    if N == 1:
        return 1
    if N == 2:
        return 2

    result = func(int(N/3)) + func(N-1)
    return result

print(func(N))