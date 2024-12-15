def even_or_odd(n):
    if n % 2 == 0:
        return 1 if (n // 2) % 2 == 1 else 2
    else:
        return 0

# 테스트
n = int(input())
print(even_or_odd(n))
