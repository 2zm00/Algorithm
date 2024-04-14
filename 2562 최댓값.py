numbers = []  # 숫자를 저장할 리스트 생성

# 아홉 번의 입력을 받아 리스트에 저장
for _ in range(9):
    num = int(input())
    numbers.append(num)

# 최댓값과 해당 수의 인덱스 출력
max_num = max(numbers)
max_index = numbers.index(max_num) + 1
print(max_num)  # 최댓값 출력
print(max_index)  # 최댓값의 인덱스 출력