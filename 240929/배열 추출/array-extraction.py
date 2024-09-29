import heapq


n = int(input())


pq = []



for i in range(n) :
    k = int(input())


    if k == 0 :
        if len(pq) == 0 :
            print(0)
        
        else :
            print(-pq[0])
            heapq.heappop(pq)
    
    else :
        heapq.heappush(pq, -k)