import sys



value = 0

n = int(input())

lst = list(map(int, input().split()))

index=sys.maxsize

while index != 0 :
    maxi = max(lst)
    index = lst.index(maxi)
    print(index+1, end= " ")
    lst = lst[:index]