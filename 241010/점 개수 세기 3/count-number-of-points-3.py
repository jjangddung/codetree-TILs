from sortedcontainers import SortedSet


n,q = map(int, input().split())


points = list(map(int, input().split()))


for _ in range(q) :

    nums = SortedSet()
    mapper = dict()
    cnt = 1
    for p in points :
        nums.add(p)
    s , e = map(int, input().split())

    nums.add(s)
    nums.add(e)

    for num in nums :
        mapper[num] = cnt

        cnt +=1
    
    print(mapper[e]- mapper[s]+1)