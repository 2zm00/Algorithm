from collections import Counter

# 입력 받기
dice = list(map(int, input().split()))

# 상금 계산 함수
def calculate_prize(dice):
    # 주사위 눈의 개수를 세기
    counter = Counter(dice)
    # 가장 많이 나온 주사위 눈의 개수
    max_count = max(counter.values())
    
    if max_count == 3:  # 같은 눈이 3개
        number = dice[0]  # 모두 같으므로 아무 숫자나 사용 가능
        return 10000 + number * 1000
    elif max_count == 2:  # 같은 눈이 2개
        for num in counter:
            if counter[num] == 2:
                return 1000 + num * 100
    else:  # 모두 다른 눈
        return max(dice) * 100

# 상금 계산 및 출력
print(calculate_prize(dice))