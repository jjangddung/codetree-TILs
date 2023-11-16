import sys

input = sys.stdin.readline

a,b,c,d = map(int, input().split())

num_1 = 60*a + b
num_2 = 60*c + d
print(num_2-num_1)