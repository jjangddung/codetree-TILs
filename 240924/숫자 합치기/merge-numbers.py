import sys
import heapq

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 최소 힙으로 변환
heapq.heapify(lst)

result = 0

while len(lst) > 1:
    # 가장 작은 두 값을 꺼내서 더함
    value1 = heapq.heappop(lst)
    value2 = heapq.heappop(lst)
    value = value1 + value2
    result += value
    # 더한 값을 다시 힙에 넣음
    heapq.heappush(lst, value)

print(result)