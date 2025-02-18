N = int(input())

# 가로 부분 출력 (상단)
for i in range(N):
    print('@' * (N * 5))

# 세로 부분 출력 (왼쪽)
for i in range(N * 4):
    print('@' * N)
