import sys




n,s = map(int, input().split())

grid = list(map(int, input().split()))

mini = sys.maxsize



for i in range(n) :
    for j in range(i+1,n) :
        num = 0

        for v  in range(n) :
            if v == i or v == j :
                continue
            num += grid[v]

        # num = grid[i] + grid[j]
        result = abs(num - s)
        mini = min(result,mini)


print(mini)