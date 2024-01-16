def generate_grid(n):
    # n x n 크기의 2차원 리스트를 1로 초기화
    grid = [[1] * n for _ in range(n)]

    # 격자 값 계산
    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1] + grid[i-1][j-1]

    return grid

def print_grid(grid):
    for row in grid:
        for value in row:
            print(value, end=' ')
        print()

def main():
    try:
        # 사용자로부터 n 입력 받기
        n = int(input())

        # 격자 생성 및 출력
        grid = generate_grid(n)
        # print("\n생성된 격자:")
        print_grid(grid)

    except ValueError:
        print("올바른 정수를 입력하세요.")

if __name__ == "__main__":
    main()