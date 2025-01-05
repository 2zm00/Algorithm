import math

def calculate_a2_minus_b2(T):
    # T = 2 * sqrt(a^2 - b^2)
    # 따라서 a^2 - b^2 = (T/2)^2
    result = (T / 2) ** 2
    return result

# 입력 받기
T = int(input())
# 결과 계산
result = calculate_a2_minus_b2(T)
# 반올림하여 정수로 출력
print(round(result))
