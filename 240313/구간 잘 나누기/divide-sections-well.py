import sys


input = sys.stdin.readline





n,m = map(int , input().split())
arr = list(map(int , input().split()))


def check(arr, n, m, mid):
    count = 1
    total = 0
    
    for num in arr:
        total += num
        if total > mid: #mid값을 기준으로 판별
            count += 1
            total = num
        if count > m:
            return False
    
    return True

def min_max_sum(arr, n, m):
    low = max(arr)  # 가능한 최소값
    high = sum(arr)  # 가능한 최대값
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if check(arr, n, m, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result

# 예시 입력


print(min_max_sum(arr, n, m))  # 출력: 5