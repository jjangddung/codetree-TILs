from sortedcontainers import SortedSet


n,q = map(int, input().split())


points = list(map(int, input().split()))



nums = SortedSet()


for p in points :
    nums.add(p)

# 사용되는 모든 번호를 treeset에 넣어줍니다.
# for v1, v2 in edges:
    # nums.add(v1)
    # nums.add(v2)
# 
# treeset에서 정점을 작은 번호부터 뽑으면서
# 각 정점별로 1번부터 순서대로 매칭하여
# 그 결과를 hashmap에 넣어줍니다.
mapper = dict()
cnt = 1
for num in nums:
    mapper[num] = cnt
    # 기존 정점번호마다 어떤 번호로
    # 정해졌는지를 출력해봅니다.
    # print(num, "->", cnt)
    cnt += 1

# 주어진 간선을 이루는 정점 번호를
# 새로운 정점 번호로 변경해줍니다.
for _ in range(q) :
    s , e = map(int, input().split())
    count = 0
    for v in range(s,e+1) :
        if v in mapper :
            count +=1
        
    print(count)