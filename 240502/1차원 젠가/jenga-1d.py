import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))


first = list(map(int, input().split()))
second = list(map(int, input().split()))
temp = []

for t in range(first[0],first[1]+1) :
    arr[t-1] = 0

for i in range(n) :
    if arr[i] != 0 :
        temp.append(arr[i])

length = len(temp)

new_temp = []

for j in range(second[0],second[1]+1) :
    temp[j-1] = 0

for j in range(length) :
    if temp[j] != 0 :
        new_temp.append(temp[j])

print(len(new_temp))
for result in new_temp :
    print(result)