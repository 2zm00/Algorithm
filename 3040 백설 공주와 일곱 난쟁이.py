def find_seven_dwarfs(numbers):
    # 아홉 난쟁이의 총합 계산
    total_sum = sum(numbers)
    
    # 두 숫자를 제외한 나머지 7개의 합이 100이어야 하므로
    # 제외할 두 숫자를 찾는다.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if total_sum - (numbers[i] + numbers[j]) == 100:
                # 두 숫자를 제외하고 나머지 숫자를 반환
                result = [numbers[k] for k in range(len(numbers)) if k != i and k != j]
                return sorted(result)  # 정렬된 결과 반환

# 입력 받기
numbers = []
for _ in range(9):
    numbers.append(int(input()))

# 함수 호출 및 출력
result = find_seven_dwarfs(numbers)
for num in result:
    print(num)
