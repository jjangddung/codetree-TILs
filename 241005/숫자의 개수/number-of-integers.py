import sys
import bisect

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# m개의 숫자에 대한 입력
queries = [int(sys.stdin.readline().strip()) for _ in range(m)]

# 각 숫자가 몇 번 나왔는지 출력
for query in queries:
    left = bisect.bisect_left(numbers, query)
    right = bisect.bisect_right(numbers, query)
    print(right - left)