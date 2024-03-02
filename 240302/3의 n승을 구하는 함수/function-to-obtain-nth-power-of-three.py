import sys

n = int(input())


def func(n) :
    if n == 0 :
        return 1
    result = 3*func(n-1)

    return result


print(func(n))