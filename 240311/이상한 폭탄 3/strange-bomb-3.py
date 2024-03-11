import sys

input = sys.stdin.readline

n,k = map(int,input().split())

bomb_list = [int(input()) for _ in range(n)]

bomb = set(bomb_list)
bomb = list(bomb)
bomb.sort()

maxi = 0
real = 0

t = (maxi, real)
for b in bomb :
    num_list = []
    t = (maxi,real)
    

    for num,ele in enumerate(bomb_list) :
        if ele == b :
            num_list.append(num)
    length = len(num_list)
    count = 1
    for c in range(1,length) :
        if num_list[c] - num_list[c-1] <= k :
            count +=1
    if t[0] < count :
        maxi = count
        real = b
    elif t[0] == count :
        if t[1] < b :
            maxi = count
            real = b

print(t[1])