import sys

n, m = map(int, input().split())

d = {}

# n개의 단어와 인덱스 저장
for i in range(n):
    d[input().strip()] = i + 1  # 입력값을 딕셔너리에 저장

# m개의 질문 처리
for _ in range(m):
    query = input().strip()

    try:
        t = int(query)  # 숫자일 경우
        for key, value in d.items():
            if t == value:
                print(key)
                break  # 첫 번째 일치하는 key를 찾으면 루프 종료
    except ValueError:
        # 문자열일 경우 딕셔너리에서 key로 검색
        print(d[query])