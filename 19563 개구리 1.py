def can_frog_reach(a, b, c):
    # 맨해튼 거리 계산
    manhattan_distance = abs(a) + abs(b)
    
    # 조건 1: 맨해튼 거리는 점프 횟수를 초과할 수 없음
    if manhattan_distance > c:
        return "NO"
    
    # 조건 2: 맨해튼 거리와 점프 횟수의 홀짝성이 같아야 함
    # (점프 횟수 - 맨해튼 거리)가 짝수여야 함
    if (c - manhattan_distance) % 2 != 0:
        return "NO"
    
    return "YES"

# 입력 받기
a, b, c = map(int, input().split())

# 결과 출력
print(can_frog_reach(a, b, c))
