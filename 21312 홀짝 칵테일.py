def get_cocktail_taste(a, b, c):
    # 모든 경우의 수를 고려하여 최대 곱을 찾는 함수
    numbers = [a, b, c]
    max_odd = -1  # 홀수 최대값
    max_even = -1  # 짝수 최대값
    
    # 1개 선택
    for i in range(3):
        product = numbers[i]
        if product % 2 == 1:  # 홀수
            max_odd = max(max_odd, product)
        else:  # 짝수
            max_even = max(max_even, product)
    
    # 2개 선택
    for i in range(3):
        for j in range(i + 1, 3):
            product = numbers[i] * numbers[j]
            if product % 2 == 1:  # 홀수
                max_odd = max(max_odd, product)
            else:  # 짝수
                max_even = max(max_even, product)
    
    # 3개 선택
    product = a * b * c
    if product % 2 == 1:  # 홀수
        max_odd = max(max_odd, product)
    else:  # 짝수
        max_even = max(max_even, product)
    
    # 홀수가 있으면 홀수 중 최대값 반환
    if max_odd != -1:
        return max_odd
    # 홀수가 없으면 짝수 중 최대값 반환
    return max_even

# 입력 받기
a, b, c = map(int, input().split())
print(get_cocktail_taste(a, b, c))
