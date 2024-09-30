import heapq


n = int(input())



pq = []

grid = list(map(int, input().split()))


for g in grid :
    heapq.heappush(pq,-g)



while len(pq) > 1 :
    num1 = -pq[0]
    num2 = -pq[1]
    num3 = num1-num2
    heapq.heappop(pq)
    heapq.heappop(pq)
    heapq.heappush(pq,-num3)



if len(pq) == 0 :
    print(-1)

else :
    print(-pq[0])