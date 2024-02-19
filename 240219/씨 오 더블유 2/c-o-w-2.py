import sys


input = sys.stdin.readline


n = int(input())

count = 0
arr = input()

for i in range(n-2) :
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            result = arr[i] + arr[j] + arr[k]
            # print(result)

            if result == "COW" :
                count +=1


print(count)