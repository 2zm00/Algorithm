import sys

# 입력 받기
n = int(sys.stdin.readline())
numbers = [0] * 10001  # 카운팅 정렬을 위한 배열

# 숫자 카운팅
for _ in range(n):
    num = int(sys.stdin.readline())
    numbers[num] += 1

# 정렬된 결과 출력
for i in range(10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)