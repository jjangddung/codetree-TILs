import sys

input  = sys.stdin.readline

n,s = map(int, input().split())

arr = list(map(int, input().split()))

maximum = 10000000

standard = abs(sum(arr) - arr[0] - arr[1] -s)

for i in range(n-1) :
    for j in range(i+1,n) :
        result = sum(arr)

        first = arr[i]
        second = arr[j]
        # standard = abs(first-second)
        new = result - first - second
        if abs(new-s) < standard :
            final = new-s
            standard = final
        
    
print(final)