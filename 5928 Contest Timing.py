from datetime import datetime

def calculate_contest_duration(end_day, end_hour, end_minute):
    # 시작 시간: 11/11/11 11:11 AM
    start_time = datetime(2011, 11, 11, 11, 11)
    # 종료 시간
    end_time = datetime(2011, 11, end_day, end_hour, end_minute)
    
    # 분 단위로 차이 계산
    duration = (end_time - start_time).total_seconds() / 60
    
    # 종료 시간이 시작 시간보다 이전이면 -1 반환
    if duration < 0:
        return -1
    else:
        return int(duration)

# 입력 받기
D, H, M = map(int, input().split())
print(calculate_contest_duration(D, H, M))
