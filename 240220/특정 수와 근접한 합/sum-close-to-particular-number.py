import sys

input  = sys.stdin.readline

n,s = map(int, input().split())

arr = list(map(int, input().split()))

total =sum(arr) 
standard = abs(total - arr[0] - arr[1] -s)

for i in range(n-1) :
    for j in range(i+1,n) :

        first = arr[i]
        second = arr[j]
        # standard = abs(first-second)
        new = total - first - second
        if abs(new-s) < standard :
            final = abs(new-s)
            standard = final
        
    
print(final)