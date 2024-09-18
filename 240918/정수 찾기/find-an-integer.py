import sys

n1= int(input())

lst1 = list(map(int, input().split()))

lst1 = set(lst1)
n2 = int(input())

lst2 = list(map(int, input().split()))



for l in lst2 :
    if l in lst1 :
        print(1)
    
    else :
        print(0)