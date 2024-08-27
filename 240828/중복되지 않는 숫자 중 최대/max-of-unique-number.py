n = int(input())


lst1 = list(map(int, input().split()))

maxi = 0

for l in lst1 :
    if lst1.count(l) == 1 :
        maxi = max(l,maxi)


if maxi == 0 :
    print(-1)

else :
    print(maxi)