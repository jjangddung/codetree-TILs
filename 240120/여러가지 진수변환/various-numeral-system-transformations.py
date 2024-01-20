import sys

input = sys.stdin.readline


n,b = map(int, input().split())


digit_list = []

while True :
    if n < b :
        digit_list.append(n)
        break
    digit = n%b
    n = n//b
    digit_list.append(digit)


for i in digit_list[::-1] :
    print(i, end= "")