# 다섯 개의 수를 입력받아 리스트에 저장
numbers = []
for _ in range(5):
    numbers.append(int(input()))

# 평균 계산 (정수 나눗셈 사용)
average = sum(numbers) // len(numbers)

# 중앙값 계산
sorted_numbers = sorted(numbers)
median = sorted_numbers[len(sorted_numbers) // 2]

# 결과 출력
print(average)
print(median)
