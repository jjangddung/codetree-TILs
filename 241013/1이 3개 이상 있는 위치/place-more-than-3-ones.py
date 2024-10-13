def count_adjacent_cells_with_ones(n, grid):
    # 방향 벡터: 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0

    # 각 칸을 순회하면서 상하좌우 1의 개수를 센다
    for i in range(n):
        for j in range(n):
            # 현재 칸에서 상하좌우 1의 개수를 센다
            adjacent_ones = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                # 격자 범위를 벗어나지 않는지 체크
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        adjacent_ones += 1
            # 상하좌우에 1이 3개 이상이면 카운트 증가
            if adjacent_ones >= 3:
                count += 1
    
    return count

# 입력 받기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
result = count_adjacent_cells_with_ones(n, grid)
print(result)