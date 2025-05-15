# 3번
"""
페이지 되돌리기
문제 설명
웹 브라우저를 개발 중인 당신은 사용자가 웹 페이지를 탐색하는 데 걸리는 총 시간을 계산하는 기능을 구현해야 합니다. 사용자는 여러 페이지를 순서대로 방문하며, 이미 방문했던 페이지로 되돌아갈 수도 있습니다. 처음 방문하는 페이지는 탐색하는 데 t초가 걸리지만, 이미 방문했던 페이지로 되돌아가는 데는 1초밖에 걸리지 않습니다.

사용자가 방문하는 페이지 수 n, 처음 방문하는 페이지 탐색 시간 t, 그리고 사용자가 방문하는 페이지 목록이 주어졌을 때, 총 탐색 시간을 계산하는 프로그램을 작성하세요.

입력 형식
첫 번째 줄에는 페이지 수 n과 처음 방문하는 페이지 탐색 시간 t가 공백으로 구분되어 주어집니다. (1 ≤ n ≤ 100, 1 ≤ t ≤ 100)

두 번째 줄에는 사용자가 방문하는 페이지 번호가 공백으로 구분되어 주어집니다. 페이지 번호는 1 이상의 정수이며, 최대 1000까지 가능합니다.

출력 형식
총 탐색 시간을 초 단위로 출력합니다.
"""

def calculate_time(n, t, pages):
    total_time = 0
    visited = set()

    for page in pages:
        if page in visited:
            total_time += 1
        else:
            total_time += t
            visited.clear()  # 방문 기록 초기화
            visited.add(page)
    return total_time

# 예시 입력
n = 6
t = 10
pages = [1, 2, 3, 1, 2, 4]

result = calculate_time(n, t, pages)
print(f"총 소요 시간: {result}초")  # 출력: 총 소요 시간: 52초


# 4번
"""
돗자리 펼치기
문제 설명
넓은 마당에 돗자리를 펴려고 합니다. 마당은 격자 모양으로 되어 있으며, 어떤 칸에는 돌멩이가 놓여 있어 돗자리를 펼 수 없습니다. 당신은 이 마당에 돌멩이를 피해서 펼칠 수 있는 가장 넓은 직사각형 모양의 돗자리를 찾고, 그 넓이와 돗자리의 가장 왼쪽 위 모서리 좌표를 출력해야 합니다. 돗자리는 반드시 격자의 선과 평행하게 놓여야 합니다.

입력 형식
첫째 줄에는 마당의 세로 길이 R과 가로 길이 C가 공백으로 구분되어 주어집니다. (1 ≤ R, C ≤ 50)

둘째 줄부터 R개의 줄에 걸쳐, 각 줄에는 C개의 정수가 공백으로 구분되어 주어집니다.

0은 빈 칸을 의미합니다.

1은 돌멩이가 있는 칸을 의미합니다.

출력 형식
첫째 줄에 펼칠 수 있는 돗자리의 최대 넓이를 출력합니다.

둘째 줄에 해당 돗자리의 가장 왼쪽 위 모서리 좌표 (행, 열)을 공백으로 구분하여 출력합니다. 좌표는 1부터 시작합니다.

만약 최대 넓이를 가지는 돗자리가 여러 개일 경우, 가장 위쪽(행 번호가 작은)에 있는 돗자리를 우선으로 합니다. 행 번호가 같다면, 가장 왼쪽(열 번호가 작은)에 있는 돗자리를 선택합니다.

만약 돗자리를 전혀 펼 수 없는 경우 (즉, 최대 넓이가 0인 경우), 첫째 줄에 0을 출력하고 둘째 줄은 출력하지 않습니다. 
"""

def solve():
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(list(map(int, input().split())))

    dp = [[0] * c for _ in range(r)]
    max_area = 0
    top_left_row = -1
    top_left_col = -1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                if dp[i][j] > max_area:
                    max_area = dp[i][j]
                    top_left_row = i - dp[i][j] + 2
                    top_left_col = j - dp[i][j] + 2

    print(max_area * max_area)  # 넓이는 변의 길이의 제곱
    if top_left_row != -1 and top_left_col != -1:
        print(top_left_row, top_left_col)

solve()
