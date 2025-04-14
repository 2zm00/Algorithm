# 입력 받기
n = int(input())

# 초기화
count = 0
current_num = n

# 더하기 사이클 연산 반복
while True:
    # 십의 자리와 일의 자리 분리
    a = current_num // 10  # 몫 (십의 자리)
    b = current_num % 10   # 나머지 (일의 자리)

    # 각 자리 수의 합 계산
    sum_digits = a + b

    # 새로운 수 생성: (원래 수의 일의 자리 * 10) + (합의 일의 자리)
    new_num = (b * 10) + (sum_digits % 10)

    # 사이클 카운트 증가
    count += 1

    # 현재 수를 새로운 수로 업데이트
    current_num = new_num

    # 종료 조건: 새로운 수가 처음 입력받은 수와 같으면 반복 종료
    if current_num == n:
        break

# 결과(사이클 길이) 출력
print(count)
