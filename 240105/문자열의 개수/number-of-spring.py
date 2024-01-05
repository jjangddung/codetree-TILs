count = 0  # 문자열 개수를 저장할 변수 초기화
strings = []  # 입력된 문자열을 저장할 리스트 초기화

while True:
    input_str = input()
    
    if input_str == '0':
        break  # '0'이 입력되면 루프 종료
    
    count += 1  # 문자열 개수 증가
    strings.append(input_str)  # 입력된 문자열을 리스트에 추가

print(count)

# 홀수 번째 문자열 출력
# print("홀수 번째 문자열:")
for i in range(0, count, 2):
    print(strings[i])