import heapq

n,m = map(int, input().split())

arr = list(map(int, input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem) # priority queue에 넣어줍니다.

    # print(-pq[0], end=" ")    # 최댓값을 출력합니다.


for _ in range(m) :
    value = pq[0]
    heapq.heappop(pq)
    heapq.heappush(pq, value +1)

print(-pq[0])