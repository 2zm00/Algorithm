# 행렬의 크기 N과 M 입력 받기
N, M = map(int, input().split())

# 행렬 A 입력 받기
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B 입력 받기
B = [list(map(int, input().split())) for _ in range(N)]

# 행렬 A와 B 더하기
result = []
for i in range(N):
    result_row = []
    for j in range(M):
        result_row.append(A[i][j] + B[i][j])
    result.append(result_row)

# 결과 출력
for row in result:
    print(*row)
