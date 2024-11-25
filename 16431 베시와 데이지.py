# 입력 받기
Br, Bc = map(int, input().split())  # 베시의 위치
Dr, Dc = map(int, input().split())  # 데이지의 위치
Jr, Jc = map(int, input().split())  # 존의 위치

# 베시의 최단 거리 계산 (체스의 킹처럼 이동 - 8방향)
# 대각선 이동이 가능하므로 row, col의 차이 중 큰 값이 최단 거리
bessie_distance = max(abs(Br - Jr), abs(Bc - Jc))

# 데이지의 최단 거리 계산 (상하좌우 이동 - 맨해튼 거리)
# 행 차이 + 열 차이가 최단 거리
daisy_distance = abs(Dr - Jr) + abs(Dc - Jc)

# 결과 출력
if bessie_distance < daisy_distance:
    print('bessie')
elif daisy_distance < bessie_distance:
    print('daisy')
else:
    print('tie')