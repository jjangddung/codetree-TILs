import sys
n, m  =map(int, input().split())
arr = list(map(int, input().split()))

    # 오른쪽 구간으로 이동해야 합

for i in range(m):
    target  = int(input())
    left, right = 0 , n-1
    idx =-2

    while left <= right :
        mid = (left + right)//2
        if arr[mid] == target :
            idx = mid
            break
        
        if arr[mid] > target :
            right  = mid -1
        
        else :
            left  = mid  +1
    print(idx-1)