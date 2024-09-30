import heapq



import sys

n = int(input())

grid = list(map(int, input().split()))



pq = []

maxi = -sys.maxsize
for k in range(1,n-1) :
    # new_grid = grid[k:]
    pq = []
    for i in range(k,n) :
        heapq.heappush(pq,grid[i])
    
    heapq.heappop(pq)
    result = sum(pq)/len(pq)
    # print(result)
    maxi = max(result,maxi)
    



print(f'{maxi:.2f}')