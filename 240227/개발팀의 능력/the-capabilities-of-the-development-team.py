import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

# 4명의 팀원으로 가능한 모든 조합을 고려하여 세 팀의 차이 중 최솟값을 찾습니다.
def diff(i, j, k, l):
    # 세 번째 팀원의 합은 전체에서 첫 번째 팀원과 두 번째 팀원의 합을 빼주면 됩니다.
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 - sum2

    # 세 팀의 합이 같은 경우 1000을 리턴합니다.
    if sum1 == sum2 or sum1 == sum3 or sum2 == sum3:
        return 10000000
    else:
        # 세 팀의 차이 중 최댓값을 리턴합니다.
        ret = abs(sum1 - sum2)
        ret = max(ret, abs(sum2 - sum3))
        ret = max(ret, abs(sum3 - sum1))
        return ret

min_diff = 10000000

# 가능한 모든 조합을 고려하여 세 팀의 차이 중 최솟값을 찾습니다.
for i in range(5):
    for j in range(i+1, 5):
        for k in range(5):
            for l in range(k+1, 5):
                # 모든 팀원이 서로 다른지 확인하고, 다르다면 세 팀의 차이를 계산합니다.
                if k == i or k == j or l == i or l == j:
                    continue
                min_diff = min(min_diff, diff(i, j, k, l))

if min_diff == 10000000 :
    print(-1)

else :
    print(min_diff)