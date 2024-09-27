from sortedcontainers import SortedSet


n,m = map(int, input().split())

grid = list(map(int, input().split()))


# 빈좌석중 최대값에 앉히기 ... ?

maxi = 0
s =  SortedSet() # 앉힌 자리로 했는데 ,,,, 빈 자리로 구성을 해볼까 >>>


for i in range(1,m+1) :
    s.add(i)


count = 0

for i in range(n) :
    t= grid[i]
    while t >  0 and t  in s : 
        s.remove(t)
        count +=1
    if t == 0 :
        break
    
    else  :
        t-=1

print(count)