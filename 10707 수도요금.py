# 입력 받기
A = int(input())  # X사의 1리터당 요금
B = int(input())  # Y사의 기본요금
C = int(input())  # Y사의 기본요금 적용 상한
D = int(input())  # Y사의 추가요금
P = int(input())  # 한 달간 수도 사용량

# X사 요금 계산
x_cost = A * P

# Y사 요금 계산
if P <= C:
    y_cost = B
else:
    y_cost = B + (P - C) * D

# 더 저렴한 요금 출력
print(min(x_cost, y_cost))