def find_max_n(s):
    n = 0
    total = 0
    
    while total <= s:
        n += 1
        total += n
    
    return n - 1

# 입력 받기
s = int(input())

# 가능한 n의 최댓값 출력
print(find_max_n(s))