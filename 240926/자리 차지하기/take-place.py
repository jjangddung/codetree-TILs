n, m = map(int, input().split())

grid = list(map(int, input().split()))

s = set()

for t in grid:
    # t에서부터 아래로 내려가면서 비어 있는 자리를 찾는다
    while t > 0 and t in s:
        t -= 1

    if t > 0:  # 0보다 크면, 해당 자리에 앉힐 수 있음
        s.add(t)

print(len(s))