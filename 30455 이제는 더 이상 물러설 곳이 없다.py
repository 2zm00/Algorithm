def solve(N):
    # N이 홀수인 경우 Goose가 승리
    # N이 짝수인 경우 Duck이 승리
    if N % 2 == 0:
        return "Duck"
    else:
        return "Goose"

# 입력 받기
N = int(input())
print(solve(N))
