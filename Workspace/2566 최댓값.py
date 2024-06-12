def find_max_in_grid(grid):
    max_value = float('-inf')  # 초기값으로 매우 작은 값을 설정
    max_position = (-1, -1)    # 초기값으로 유효하지 않은 위치를 설정
    
    for i in range(len(grid)):         # 행 반복
        for j in range(len(grid[i])):  # 열 반복
            if grid[i][j] > max_value:
                max_value = grid[i][j]
                max_position = (i, j)
    
    return max_value, max_position

# 입력 받기
grid = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

# 격자에서 최댓값과 위치 찾기
max_value, max_position = find_max_in_grid(grid)

# 결과 출력
print(max_value)
print(max_position[0] + 1, max_position[1] + 1)