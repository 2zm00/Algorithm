def calculate_change(button_presses, total_money=5000):
    # 각 버튼별 음료수 가격
    prices = {1: 500, 2: 800, 3: 1000}
    
    # 총 비용 계산
    total_cost = sum(prices[button] for button in button_presses)
    
    # 거스름돈 계산
    change = total_money - total_cost
    return change

# 입력 받기
buttons = list(map(int, input().split()))

# 거스름돈 계산 및 출력
print(calculate_change(buttons))
