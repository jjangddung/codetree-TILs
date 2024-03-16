import sys

input = sys.stdin.readline


n = int(input())

first_value = list(map(int , input().split()))
second_value = list(map(int, input().split()))

count = 0

for i in range(n-1) :
    if first_value[i] != second_value[i] :
        result = first_value[i] - second_value[i]
        first_value[i+1] += result
    count += result

print(count)