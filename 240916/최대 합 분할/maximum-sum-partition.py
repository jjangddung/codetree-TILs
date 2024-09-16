import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int, input().split()))
    total_sum = sum(nums)
    OFFSET = total_sum  # sum_diff의 음수 값을 처리하기 위한 오프셋

    MAX_SUM_DIFF = 2 * OFFSET + 1
    dp_prev = [-1] * MAX_SUM_DIFF  # dp[sum_diff + OFFSET] = max_sum_A
    dp_prev[OFFSET] = 0  # sum_diff = 0일 때, sum_A = 0

    for num in nums:
        dp_curr = dp_prev[:]
        for sum_diff in range(-OFFSET, OFFSET + 1):
            idx = sum_diff + OFFSET
            if dp_prev[idx] >= 0:
                sum_A = dp_prev[idx]

                # 그룹 A에 num을 추가
                new_sum_diff = sum_diff + num
                new_idx = new_sum_diff + OFFSET
                new_sum_A = sum_A + num
                if dp_curr[new_idx] < new_sum_A:
                    dp_curr[new_idx] = new_sum_A

                # 그룹 B에 num을 추가
                new_sum_diff = sum_diff - num
                new_idx = new_sum_diff + OFFSET
                new_sum_A = sum_A  # sum_A는 그대로
                if dp_curr[new_idx] < new_sum_A:
                    dp_curr[new_idx] = new_sum_A

                # 그룹 C에 num을 추가 (sum_diff와 sum_A 변화 없음)
                # 이미 dp_curr에 현재 상태가 있으므로 업데이트 불필요

        dp_prev = dp_curr  # dp_prev를 업데이트

    result = dp_prev[OFFSET]  # sum_diff = 0일 때의 max_sum_A
    if result == 0:
        print(0)
    else:
        print(result)

threading.Thread(target=main).start()