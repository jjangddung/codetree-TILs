import heapq



import sys

n = int(input())

grid = list(map(int, input().split()))

grid = grid[::-1]

# pq = []

maxi = -sys.maxsize
prev_sum = grid[0] + grid[1]
prev_small = min(grid[0],grid[1])

new_grid = [grid[0], grid[1]]
pq = sorted(new_grid)

# print(new_grid)
prev_avg = (prev_sum - prev_small)/1
# print(maxi)
for k in range(2,n-1) :
    heapq.heappush(pq, grid[k])
    prev_sum += grid[k]
    # print("pq: ", pq)
    num = pq[0]
    # print('num: ', num)
    result = (prev_sum-num)/(k)
    # print(result)
    # heapq.heappush(pq, num)
    maxi = max(result,maxi)
    



print(f'{maxi:.2f}')