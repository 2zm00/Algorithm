def calculate_minimum_cost(c, d):
    # 각 통신사의 요금 정보
    operators = {
        "ParsTel": {"call": 30, "data": 40},
        "ParsCell": {"call": 35, "data": 30},
        "ParsPhone": {"call": 40, "data": 20}
    }
    
    # 각 통신사별 총 비용 계산
    costs = {
        operator: c * details["call"] + d * details["data"]
        for operator, details in operators.items()
    }
    
    # 최소 비용 반환
    return min(costs.values())

# 입력 처리
while True:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    print(calculate_minimum_cost(c, d))