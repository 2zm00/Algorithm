import math

def calculate_cutting_difference(w, h):
    # 직사각형 방식으로 자르는 길이 (가로 + 세로)
    rectangle_cut = w + h
    
    # 대각선으로 자르는 길이 (피타고라스 정리)
    diagonal_cut = math.sqrt(w**2 + h**2)
    
    # 두 방식의 차이 계산
    return rectangle_cut - diagonal_cut

# 입력 받기
w, h = map(int, input().split())

# 결과 출력 (소수점 아래 9자리까지 출력)
print(calculate_cutting_difference(w, h))