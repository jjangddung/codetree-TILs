import heapq



import sys

n = int(input())

grid = list(map(int, input().split()))



pq = []

maxi = -sys.maxsize
for k in range(1,n-1) :
    new_grid = grid[k:]
    pq = []
    for g in new_grid :
        heapq.heappush(pq,g)
    
    heapq.heappop(pq)
    result = sum(pq)/len(pq)
    # print(result)
    maxi = max(result,maxi)
    



print(f'{maxi:.2f}')