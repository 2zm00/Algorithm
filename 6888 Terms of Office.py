def find_all_positions_change(X, Y):
    # X년도부터 시작하여 최소공배수(60)의 배수만큼 증가하며 찾기
    result = []
    period = 60  # 2, 3, 4, 5의 최소공배수
    
    current = X
    while current <= Y:
        result.append(current)
        current += period
    
    return result

# 입력 처리
X = int(input())
Y = int(input())

# 결과 출력
years = find_all_positions_change(X, Y)
for year in years:
    print(f"All positions change in year {year}")
