def solve():
    n = int(input())  # 색종이 수

    # 도화지 초기화 (100x100)
    paper = [[0] * 100 for _ in range(100)]

    for _ in range(n):
        x, y = map(int, input().split())  # 색종이 위치 (왼쪽 변 거리, 아래쪽 변 거리)

        # 색종이 붙이기
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                paper[i][j] = 1

    # 넓이 계산
    area = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j] == 1:
                area += 1

    print(area)

solve()
