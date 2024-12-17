def count_minutes_with_digit(start_hour, start_minute, end_hour, end_minute, digit):
    count = 0
    # 시작 시간부터 종료 시간까지 순회
    for hour in range(start_hour, end_hour + 1):
        # 분 순회 (0~59)
        for minute in range(60):
            # 종료 시간에 도달하면 반복 중단
            if hour == end_hour and minute > end_minute:
                break
            # 시작 시간 이전은 건너뛰기
            if hour == start_hour and minute < start_minute:
                continue
            # 시간을 HH:MM 형태의 문자열로 변환
            time_str = f"{hour:02}:{minute:02}"
            # 찾고자 하는 숫자가 시간 문자열에 있는지 확인
            if str(digit) in time_str:
                count += 1
    return count

# 입력 받기
start_hour, start_minute = map(int, input().split())
end_hour, end_minute = map(int, input().split())
n = int(input())

# 결과 출력
result = count_minutes_with_digit(start_hour, start_minute, end_hour, end_minute, n)
print(result)
