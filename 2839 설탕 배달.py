def min_bags(n):
    # 3kg 미만은 배달 불가능
    if n < 3:
        return -1
        
    # 우선 5kg 봉지를 최대한 사용
    봉지5kg = n // 5
    남은무게 = n % 5
    
    # 5kg 봉지를 하나씩 줄여가며 3kg 봉지 조합 시도
    while 봉지5kg >= 0:
        if 남은무게 % 3 == 0:
            return 봉지5kg + (남은무게 // 3)
        봉지5kg -= 1
        남은무게 += 5
        
    return -1

# 입력받고 결과 출력
n = int(input())
print(min_bags(n))