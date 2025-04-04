def prime_factorization(n):
    if n == 1:
        return
    
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i)
            n //= i
        i += 1
    
    if n > 1:
        print(n)

N = int(input())
prime_factorization(N)
