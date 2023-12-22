import sys

input = sys.stdin.readline


map_list = []

for i in range(4) :
    a_list = list(map(int, input().split()))
    result = sum(a_list)
    print(result)