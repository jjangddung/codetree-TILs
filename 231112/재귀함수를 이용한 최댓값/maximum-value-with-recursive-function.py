import sys

input = sys.stdin.readline


N = int(input())

_list = list(map(int, input().split()))


def f(num,l) :
    if num == 1 :
        return l[0]

    return max(l[num-1],f(num-1,l))



print(f(N,_list))