# 입력 받기
N = int(input())
arr = list(map(int, input().split()))

# 전체 합 계산: 1부터 N까지의 합
total_sum = N * (N + 1) // 2

# 누락된 숫자 계산
missing_number = total_sum - sum(arr)

# 결과 출력
print(missing_number)
