import sys

input = sys.stdin.readline


n = int(input())

height_list = []

for _ in range(n) :
    height_list.append(int(input()))

low_height  = min(height_list)
high_height = max(height_list)

maxi = 0

for h in range(low_height,high_height+1) :
    count = 0
    new_height_list = []
    for j in range(n) :
        if arr[j] - h > 0 :
            new_height = 1
        else :
            new_height = 0
        new_height_list.append(new_height)
    for p in range(n) :
        if arr[p] == 1 :

            if p == n-1 :
                if arr[p-1] != 1 and arr[p] == 1:
                    count +=1

            else :    
                if arr[p+1] != 1 :
                    count +=1