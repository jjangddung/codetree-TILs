import heapq


n,m = map(int, input().split())

point_lst = [
    list(map(int, input().split()))
    for _ in range(n)
]


pq = []

for  i in range(n) :
    x = point_lst[i][0]
    y = point_lst[i][1]
    distance = abs(x) + abs(y)
    heapq.heappush(pq, [distance,x,y])


for i in range(m) :
    dis,x,y = pq[0]
    # print(x,y)
    new_x, new_y = x + 2 , y + 2
    dis = abs(new_x) + abs(new_y)
    heapq.heappop(pq)
    heapq.heappush(pq, [dis,new_x,new_y])


dis,x,y = pq[0]

print(x,y)