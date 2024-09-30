import heapq


n = int(input())



pq = []

grid = list(map(int, input().split()))


for g in grid :
    heapq.heappush(pq,-g)


# print(pq)

while len(pq) > 1 :
    # num1 = -pq[0]
    # num2 = -pq[1]
    
    num1 = -heapq.heappop(pq)
    num2 = -heapq.heappop(pq)
    num3 =  num1-num2
    if num3 != 0 :
        heapq.heappush(pq,-num3)
    
    



if len(pq) == 0 :
    print(-1)

else :
    print(-pq[0])