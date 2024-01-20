import sys


input = sys.stdin.readline

arr = str(input())


length = len(arr)

sum = 0

for i in range (length) :
    multiple = 2**(length-1-i)
    sum += int(arr[i])*multiple

print(sum)