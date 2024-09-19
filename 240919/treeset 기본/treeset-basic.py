from sortedcontainers import SortedSet

s = SortedSet()  # TreeSet 선언
n = int(input())  # 명령어 개수 입력

for _ in range(n):
    command = input().split()  # 명령어를 공백으로 분리
    order = command[0]  # 명령어
    value = int(command[1]) if len(command) > 1 else None  # 값이 있으면 값 할당

    if order == "add":
        s.add(value)  # 중복 값은 자동으로 무시됨

    elif order == 'remove':
        if value in s:
            s.remove(value)  # 값이 있으면 제거

    elif order == 'find':
        print("true" if value in s else "false")  # 존재 여부 출력

    elif order == 'lower_bound':
        idx = s.bisect_left(value)  # x보다 크거나 같은 값의 인덱스
        if idx < len(s):  # 인덱스가 유효하면
            print(s[idx])
        else:
            print("None")  # 없으면 None 출력

    elif order == 'upper_bound':
        idx = s.bisect_right(value)  # x보다 큰 값의 인덱스
        if idx < len(s):  # 인덱스가 유효하면
            print(s[idx])
        else:
            print("None")  # 없으면 None 출력

    elif order == 'largest':
        if len(s) > 0:  # 셋이 비어 있지 않으면
            print(s[-1])  # 마지막 값(가장 큰 값) 출력
        else:
            print("None")  # 셋이 비어 있으면 None 출력

    elif order == 'smallest':
        if len(s) > 0:  # 셋이 비어 있지 않으면
            print(s[0])  # 첫 번째 값(가장 작은 값) 출력
        else:
            print("None")  # 셋이 비어 있으면 None 출력