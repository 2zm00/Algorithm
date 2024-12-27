import math

def calculate_track_perimeter(d1, d2):
    PI = 3.141592
    # 직사각형 부분: 2 * d1
    # 반원 부분: π * d2 * 2 (원의 둘레의 절반이 2개)
    perimeter = (2 * d1) + (2 * PI * d2)
    return perimeter

# 입력 받기
d1 = int(input())
d2 = int(input())

# 결과 출력
result = calculate_track_perimeter(d1, d2)
print(result)