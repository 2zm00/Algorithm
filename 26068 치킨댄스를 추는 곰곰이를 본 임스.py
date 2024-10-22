# 기프티콘 개수 입력 받기
N = int(input())

# 사용 가능한 기프티콘 개수 초기화
usable_coupons = 0

# N번 반복하며 각 기프티콘의 유효기간 확인
for _ in range(N):
    expiry = input().strip()
    days_left = int(expiry.split('-')[1])  # D-xx 형식에서 xx 부분 추출
    
    # 유효기간이 90일 이하인 경우 사용 가능한 기프티콘으로 카운트
    if days_left <= 90:
        usable_coupons += 1

# 사용 가능한 기프티콘 개수 출력
print(usable_coupons)