def calculate_sushi_cost(red, green, blue):
    cost_red = red * 3      # 빨간 접시 비용
    cost_green = green * 4  # 초록 접시 비용
    cost_blue = blue * 5    # 파란 접시 비용
    total_cost = cost_red + cost_green + cost_blue
    return total_cost

# 입력 받기
red = int(input())    # 빨간 접시 수
green = int(input())  # 초록 접시 수
blue = int(input())   # 파란 접시 수

# 결과 출력                                                                
print(calculate_sushi_cost(red, green, blue))