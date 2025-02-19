# 기차 내 현재 승객 수와 최대 승객 수를 저장하는 변수 초기화
current_passengers = 0
max_passengers = 0

# 10개의 정류장을 순서대로 처리
for _ in range(10):
    off, on = map(int, input().split())  # 내린 사람 수, 탄 사람 수 입력받기
    current_passengers -= off           # 내린 사람 수 빼기
    current_passengers += on            # 탄 사람 수 더하기
    max_passengers = max(max_passengers, current_passengers)  # 최대 승객 수 갱신

# 최대 승객 수 출력
print(max_passengers)
