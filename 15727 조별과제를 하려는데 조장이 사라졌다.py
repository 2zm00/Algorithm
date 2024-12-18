import math

L = int(input())  # 거리 입력받기

# 성우는 1분에 최대 5만큼 이동 가능
max_speed = 5

# 최소 시간 계산
# 최대 속도로 갈 때 걸리는 시간의 올림값이 답
min_time = math.ceil(L / max_speed)

print(min_time)
