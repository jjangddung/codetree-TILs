import heapq



import sys

n = int(input())

grid = list(map(int, input().split()))

grid = grid[::-1]

pq = []

maxi = -sys.maxsize
for k in range(2,n-1) :
    new_grid = grid[:k]
    pq = []
    for i in range (len(new_grid)) :
        heapq.heappush(pq,new_grid[i])
    
    heapq.heappop(pq)
    result = sum(pq)/len(pq)
    # print(result)
    maxi = max(result,maxi)
    



print(f'{maxi:.2f}')