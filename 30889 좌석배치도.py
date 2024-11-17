# 좌석 수 입력받기
N = int(input())

# 10x20 크기의 좌석 배치도 초기화
seating_chart = [['.' for _ in range(20)] for _ in range(10)]

# N개의 예매 정보 처리
for _ in range(N):
    seat = input()
    # 행 번호 계산 (A=0, B=1, ...)
    row = ord(seat[0]) - ord('A')
    # 열 번호 계산 (1부터 시작하므로 1을 빼줌)
    col = int(seat[1:]) - 1
    # 예매된 좌석 표시
    seating_chart[row][col] = 'o'

# 좌석 배치도 출력
for row in seating_chart:
    print(''.join(row))


