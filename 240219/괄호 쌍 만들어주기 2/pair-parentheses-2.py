import sys

input = sys.stdin.readline


arr = input()
result = []
count = 0
n = len(arr)
for i in range(n-2) :
    if arr[i:i+2] == "((" :

        for j in range(i+1,n-1) :
            if arr[j:j+2] == "))" :
                count +=1
        
    else :
        pass




print(count)