import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    a,b = map(int, input().split())
    total = 0
    for ele in range(a,b+1) :
        if ele % 2 == 0 :
            total +=ele
    print(total)