import sys

input = sys.stdin.readline

# 입력값 받기
given = str(input()).strip()
word_lst = []
math_lst = []

# 입력 문자열을 연산자와 숫자로 분리
for s in given:
    if s == '-' or s == '+' or s == '*':
        math_lst.append(s)
    else:
        word_lst.append(s)

word_set = list(set(word_lst))  # 중복 제거 후 리스트로 변환

ans_lst = []
maxi = -sys.maxsize

def backtracking(num, k):
    global maxi
    if k == 6:
        real_lst = []
        result_lst = []

        for v in word_lst:
            # 각 문자에 대해 ans_lst의 값을 실수 리스트로 변환
            if v == 'a':
                real_lst.append(str(ans_lst[0]))
            elif v == 'b':
                real_lst.append(str(ans_lst[1]))
            elif v == 'c':
                real_lst.append(str(ans_lst[2]))
            elif v == 'd':
                real_lst.append(str(ans_lst[3]))
            elif v == 'e':
                real_lst.append(str(ans_lst[4]))
            elif v == 'f':
                real_lst.append(str(ans_lst[5]))

        result_lst.append(real_lst[0])

        if len(math_lst) == 0:
            value = int(real_lst[0])
            maxi = max(value, maxi)
            return

        # 수식 리스트를 완성
        for i in range(1, len(real_lst)):
            if i - 1 < len(math_lst):  # 수식 범위가 math_lst를 넘지 않도록 범위 체크
                result_lst.append(math_lst[i - 1])
                result_lst.append(real_lst[i])

        # 수식 계산
        value = int(result_lst[0])
        for i in range(1, len(result_lst), 2):
            if result_lst[i] == '-':
                value -= int(result_lst[i + 1])
            elif result_lst[i] == '+':
                value += int(result_lst[i + 1])
            elif result_lst[i] == '*':
                value *= int(result_lst[i + 1])

        maxi = max(value, maxi)
        return

    # 가능한 값 탐색 (1부터 4까지)
    for elem in range(1, 5):
        ans_lst.append(elem)
        backtracking(elem, k + 1)
        ans_lst.pop()

if len(given) == 1:
    print(4)
else:
    backtracking(1, 0)
    print(maxi)