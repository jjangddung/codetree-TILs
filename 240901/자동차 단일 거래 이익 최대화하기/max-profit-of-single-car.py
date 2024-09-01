n = int(input())

lst = list(map(int, input().split()))
maxi = 0

for i in range(n) :
    for j in range(i+1, n) :
        value = lst[j] - lst[i]
        maxi = max(value, maxi)


print(maxi)