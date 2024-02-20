import sys

input  = sys.stdin.readline

n,s = map(int, input().split())

arr = list(map(int, input().split()))

maximum = 10000000
nx = 0
ny = 0
final = 0

for i in range(n) :
    for j in range(i+1,n) :
        result = sum(arr)

        first = arr[i]
        second = arr[j]
        standard = abs(first-second)
        new = result - first - second
        if abs(new-s) < abs(maximum-s) :
            final = new-s
            maximum = new
        
    
print(final)