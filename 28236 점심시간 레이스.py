def find_lunch_race_winner(n, m, k, class_positions):
    min_time = float('inf')
    winner = 1
    
    for i in range(k):
        floor, pos = class_positions[i]
        
        # 왼쪽 계단까지의 거리 + 내려가기 + 오른쪽으로 이동
        left_dist = pos + (floor - 1) + (m + 1)
        
        # 오른쪽 계단까지의 거리 + 내려가기 + 1(급식실)
        right_dist = (m - pos + 1) + (floor - 1) + 1
        
        # 두 경로 중 최소 시간
        total_time = min(left_dist, right_dist)
        
        if total_time < min_time:
            min_time = total_time
            winner = i + 1
        elif total_time == min_time:
            winner = min(winner, i + 1)
    
    return winner

# 입력 받기
n, m, k = map(int, input().split())
class_positions = []
for _ in range(k):
    f, d = map(int, input().split())
    class_positions.append((f, d))

# 결과 출력
print(find_lunch_race_winner(n, m, k, class_positions))
