sleep_time = int(input())  # 취침 시간
wake_time = int(input())   # 기상 시간

if sleep_time >= 20:  # 취침 시간이 20시 이후인 경우
    sleep_hours = (24 - sleep_time) + wake_time
else:  # 취침 시간이 0-3시인 경우
    sleep_hours = wake_time - sleep_time

print(sleep_hours)