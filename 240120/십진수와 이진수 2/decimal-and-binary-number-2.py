import sys

input = sys.stdin.readline

sum = 0

arr = input().rstrip()

length = int(len(arr))


for i in range(length) :
    multiple = 2**(length-1-i)
    sum += int(arr[i]) * multiple

sum = sum*17
digit_list = []
while True :
    if sum < 2 :
        digit_list.append(sum)
        break
    digit = sum % 2
    digit_list.append(digit)
    sum = sum //2


for i in digit_list[::-1] :
    print(i, end= "")