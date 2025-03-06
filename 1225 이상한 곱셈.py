# 입력받은 문자열을 공백으로 구분하여 A와 B에 할당.
A, B = input().split()

# A와 B의 각 자리수의 합 계산
sum_A = sum(int(digit) for digit in A)
sum_B = sum(int(digit) for digit in B)

# 최종 결과는 두 자리수 합의 곱
result = sum_A * sum_B

# 결과 출력
print(result)
