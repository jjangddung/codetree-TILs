import sys

input = sys.stdin.readline


str_1 = str(input().rstrip())
str_2 = str(input().rstrip())

str_1 = sorted(str_1)
str_2 = sorted(str_2)

if str_1 == str_2 :
    print('Yes')
else :
    print('No')