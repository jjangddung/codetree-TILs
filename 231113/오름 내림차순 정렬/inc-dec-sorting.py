import sys

input = sys.stdin.readline


N = int(input())

_list = list(map(int, input().split()))

_list.sort()
reverse_list = _list[::-1]

for i in _list :
    print(i , end = " ")
print()
for j in reverse_list :
    print(j, end = " ")