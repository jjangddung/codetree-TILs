import sys
from collections import deque

# 백트래킹으로 서로 다른 k개 뽑기
n, k, u, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

back_lst = []
ans_lst = []
q = deque()

def backtracking(num):
    # 더 이상 선택할 수 있는 원소의 개수가 k보다 작으면 탐색 중단
    if len(back_lst) + (n**2 - num) < k:
        return
    
    # 종료 조건: k개의 원소를 모두 선택한 경우
    if len(back_lst) == k:
        ans_lst.append(back_lst[:])  # deepcopy 대신 슬라이싱으로 복사
        return
    
    if num == n**2:  # 탐색 종료
        return
    
    # 원소를 선택한 경우
    back_lst.append(num)
    backtracking(num + 1)
    
    # 원소를 선택하지 않은 경우
    back_lst.pop()
    backtracking(num + 1)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x1, y1, x2, y2):
    if in_range(x2, y2):
        result = abs(grid[x1][y1] - grid[x2][y2])
        if u <= result <= d:
            return True
    return False

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상우하좌

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(x, y, new_x, new_y) and not visited[new_x][new_y]:
                push(new_x, new_y)

final = 0

# 백트래킹 시작
backtracking(0)

# 선택된 k개의 원소로 BFS 수행
for value in ans_lst:
    visited = [[False] * n for _ in range(n)]
    q.clear()

    # 선택된 k개의 원소를 큐에 추가
    for i in range(k):
        x = value[i] // n
        y = value[i] % n
        push(x, y)
    
    # BFS 실행
    bfs()

    # 방문한 도시 수 세기
    count = sum(sum(row) for row in visited)

    final = max(count, final)

print(final)