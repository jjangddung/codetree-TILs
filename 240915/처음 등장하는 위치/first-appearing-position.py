from sortedcontainers import SortedDict


sd = SortedDict()


n = int(input())

lst = list(map(int, input().split()))

for i in range(n) :
    if lst[i] not in sd :
        sd[lst[i]] = i+1


for key, value in sd.items() :
    print(key, value)