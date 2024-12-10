# 학생 수(N)와 카드 수(M) 입력
N, M = map(int, input().split())

# 각 학생의 번호표 입력
A = []
for _ in range(N):
    A.append(int(input()))

# 카드 규칙에 따라 번호표 교환
for i in range(1, M + 1):  # 카드 1부터 M까지 사용
    for j in range(N - 1):  # 학생들 간의 비교
        if A[j] % i > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]  # 번호표 교환

# 결과 출력
for num in A:
    print(num)