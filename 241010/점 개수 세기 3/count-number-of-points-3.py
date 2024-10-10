from sortedcontainers import SortedSet


n,q = map(int, input().split())


points = list(map(int, input().split()))
nums = SortedSet()
for p in points :
        nums.add(p)
        
for _ in range(q) :
    mapper = dict()
    cnt = 1
    
    s , e = map(int, input().split())

    nums.add(s)
    nums.add(e)

    for num in nums :
        mapper[num] = cnt

        cnt +=1
    
    print(mapper[e]- mapper[s]+1)