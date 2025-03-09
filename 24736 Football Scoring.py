# 점수 계산 함수
def calculate_score(data):
    # 각 항목에 해당하는 점수를 곱하여 총점을 계산
    T, F, S, P, C = data
    return T * 6 + F * 3 + S * 2 + P * 1 + C * 2

# 입력 처리
# 첫 번째 줄: 방문 팀 점수 데이터
visiting_team = list(map(int, input().split()))
# 두 번째 줄: 홈 팀 점수 데이터
home_team = list(map(int, input().split()))

# 점수 계산
visiting_score = calculate_score(visiting_team)
home_score = calculate_score(home_team)

# 결과 출력
print(visiting_score, home_score)
