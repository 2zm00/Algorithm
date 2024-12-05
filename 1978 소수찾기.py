# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
prime_count = 0

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

# 결과 출력
print(prime_count)