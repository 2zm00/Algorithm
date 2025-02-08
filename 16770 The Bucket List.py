import sys

# 전체 입력을 한 번에 읽어서 공백 단위로 토큰화
data = sys.stdin.read().split()
if not data:
    sys.exit(0)

# 첫 토큰은 소의 개수 N
n = int(data[0])
events = []  # (시간, 버킷 변화량) 형태의 이벤트 리스트

# 각 소마다 시작 시각에는 +b, 종료 시각에는 -b인 이벤트 생성
idx = 1
for _ in range(n):
    s = int(data[idx])
    t = int(data[idx + 1])
    b = int(data[idx + 2])
    idx += 3
    events.append((s, b))   # 소가 누적적으로 버킷 b개 사용 시작
    events.append((t, -b))  # 소가 끝나면서 b개 버킷 반환

# 시간순으로 이벤트 정렬 (문제 조건에 따라 s와 t는 모두 서로 다름)
events.sort(key=lambda x: x[0])

current_buckets = 0  # 현재 사용 중인 버킷 수
max_buckets = 0      # 지금까지 사용된 최대 버킷 수 (최종 필요한 버킷 수)
for time, delta in events:
    current_buckets += delta
    if current_buckets > max_buckets:
        max_buckets = current_buckets

sys.stdout.write(str(max_buckets))
