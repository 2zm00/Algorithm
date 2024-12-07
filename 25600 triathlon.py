N = int(input())  # 참가자 수 입력
max_score = 0

# 점수 계산 함수
def calculate_score(a, d, g):
    if a == (d + g):
        return 2 * a * (d + g)  # a가 d+g와 같으면 2배
    else:
        return a * (d + g)

# N명의 참가자 점수 계산
for _ in range(N):
    a, d, g = map(int, input().split())
    score = calculate_score(a, d, g)
    max_score = max(max_score, score)

print(max_score)