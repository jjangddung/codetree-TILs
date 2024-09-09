from collections import deque

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]  # 시계방향
    max_step = 0

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if in_range(new_x, new_y) and grid[new_x][new_y] > grid[x][y]:
            max_step = max(max_step, bfs(new_x, new_y))
    
    dp[x][y] = max_step + 1
    return dp[x][y]

final = 0
for i in range(n):
    for j in range(n):
        final = max(final, bfs(i, j))

print(final)