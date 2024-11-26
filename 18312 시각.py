def count_times_with_digit(N, K):
    count = 0
    K_str = str(K)
    # 시, 분, 초에 대해 모든 경우의 수를 확인
    for hour in range(N + 1):
        for minute in range(60):
            for second in range(60):
                time_string = f'{hour:02d}{minute:02d}{second:02d}'  # HHMMSS 형식으로 변환
                if K_str in time_string:
                    count += 1
    return count

# 입력 받기
N, K = map(int, input().split())
# 결과 출력
print(count_times_with_digit(N, K))