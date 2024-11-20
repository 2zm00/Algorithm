def calculate_tax(N):
    # 케이스 1: 전체 금액의 22% 납부
    case1 = int(N * 0.78)
    
    # 케이스 2: 80% 필요 경비 인정, 나머지 20%에 대해 22% 납부
    case2 = int(N * 0.8 + (N * 0.2 * 0.78))
    
    return case1, case2

# 입력 처리
N = int(input())

# 결과 계산
result1, result2 = calculate_tax(N)

# 출력
print(result1, result2)