from sortedcontainers import SortedSet

n, q = map(int, input().split())
points = list(map(int, input().split()))

# 중복 작업을 피하기 위해 한 번만 SortedSet을 생성
nums = SortedSet(points)

# 각 쿼리에서 추가되는 값을 미리 처리하기 위해 mapper도 한 번만 생성
mapper = dict()
cnt = 1

# nums에 미리 매핑을 만들어 놓음
for num in nums:
    mapper[num] = cnt
    cnt += 1

# 쿼리를 처리
for _ in range(q):
    s, e = map(int, input().split())

    if s not in mapper:
        nums.add(s)
        mapper[s] = cnt
        cnt += 1

    if e not in mapper:
        nums.add(e)
        mapper[e] = cnt
        cnt += 1

    print(mapper[e] - mapper[s] + 1)