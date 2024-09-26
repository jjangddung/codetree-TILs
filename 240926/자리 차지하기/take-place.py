# n은 사람의 수, m은 의자의 수
n, m = map(int, input().split())

# 각 사람이 앉고 싶은 의자의 범위를 리스트로 받습니다.
people = list(map(int, input().split()))

# 의자의 사용 여부를 확인하기 위한 배열 (0: 빈 자리, 1: 이미 사용된 자리)
seats = [0] * (m + 1)

# 앉은 사람 수
seated_count = 0

# 사람들을 원하는 자리 범위 순서로 정렬합니다.
people.sort()

# 사람들을 하나씩 배치합니다.
for p in people:
    for seat in range(p, 0, -1):
        if seats[seat] == 0:
            seats[seat] = 1
            seated_count += 1
            break

# 결과 출력
print(seated_count)