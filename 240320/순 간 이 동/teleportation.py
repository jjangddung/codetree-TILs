import sys

input = sys.stdin.readline


a,b,x,y = map(int, input().split())

num_1 = abs(b-a)

num_2 = abs(a-x) + abs(y-b)

num_3 = abs(y-a) + abs(x-b)

result = min(num_1,num_2,num_3)

print(result)