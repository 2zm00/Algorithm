N = int(input())  # 라면을 끓이는 횟수 입력
for _ in range(N):
    A, B, X = map(int, input().split())  # 라면 계수, 기본 물의 양, 끓일 라면 수 입력
    W = A * (X - 1) + B  # 라면 공식: W = A(X-1) + B
    print(W)
