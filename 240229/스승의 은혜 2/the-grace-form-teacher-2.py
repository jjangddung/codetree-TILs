import sys



input = sys.stdin.readline

n, b = map(int, input().split())


arr = [int(input()) for _ in range(n)]
arr.sort()

count = 0

for i in range(n) :
    if b >= arr[i] :
        b -= arr[i]
        count +=1
    
    else :
        if b >= arr[i]//2 :
            b -= arr[i]//2
            count +=1
            break

print(count)