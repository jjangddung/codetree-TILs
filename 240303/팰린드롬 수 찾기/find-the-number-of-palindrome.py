import sys

input = sys.stdin.readline

x,y = map(int, input().split())


count = 0

for ele in range(x,y+1) :
    ele = str(ele)
    reverse_ele = ele[::-1]

    if ele == reverse_ele :
        count +=1


print(count)