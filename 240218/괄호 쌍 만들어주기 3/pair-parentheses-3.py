import sys

input = sys.stdin.readline


arr = input()

length = len(arr)

count = 0

# print(arr)

for i in range(length-1) :
    if not arr[i] == "(" :
        pass

    else :
        for j in range(i+1,length) :
            if not arr[j] == ")" :
                pass
            else :
                count +=1


print(count)