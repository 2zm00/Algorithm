# 손님 수 입력받기
N = int(input())
# 손님들이 원하는 자리 번호 입력받기
seats = list(map(int, input().split()))

# 컴퓨터 자리 상태를 저장할 리스트 (0: 비어있음, 1: 차있음)
computers = [0] * 101
# 거절당한 손님 수
reject = 0

# 각 손님에 대해
for seat in seats:
    # 이미 자리가 차있으면
    if computers[seat] == 1:
        reject += 1
    # 자리가 비어있으면
    else:
        computers[seat] = 1

print(reject)
