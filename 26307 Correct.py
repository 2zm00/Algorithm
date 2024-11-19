def time_consumed_for_problem(HH, MM):
    # 대회 시작 시간(9:00 AM)을 분으로 변환
    contest_start = 9 * 60
    # 제출 시간을 분으로 변환  
    submission_time = HH * 60 + MM
    # 소요 시간 계산
    return submission_time - contest_start

# 입력 받기
HH, MM = map(int, input().split())
# 결과 출력
print(time_consumed_for_problem(HH, MM))