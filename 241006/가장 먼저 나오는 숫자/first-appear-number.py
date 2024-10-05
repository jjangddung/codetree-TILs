import bisect

# 입력 받기
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

# 결과 저장 리스트
results = []

# 각 질의에 대해 이진 탐색 수행
for query in queries:
    # 이진 탐색으로 최초 등장 위치 찾기
    idx = bisect.bisect_left(arr, query)
    
    # 해당 위치가 배열 안에 있고, 그 위치의 값이 query와 같으면 출력
    if idx < n and arr[idx] == query:
        results.append(idx + 1)  # 1-based index이므로 +1
    else:
        results.append(-1)

# 결과 출력
for result in results:
    print(result)