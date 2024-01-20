import sys

input =  sys.stdin.readline


a,b = map(int, input().split())


arr = input()


sum  = 0

for i in range(len(arr)) :
    multiple = a**(len(arr)-1-i)
    sum += int(arr[i])*multiple


digit_list = []

while True :
    if sum < b :
        digit_list.append(sum)
        break
    digit_list.append(sum%b)

    sum= sum//b

for j in digit_list[::-1] :
    print(j, end= "")