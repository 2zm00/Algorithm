k = int(input())
fib = [0, 1] + [0] * (k - 1)  # Initialize up to index k

for i in range(2, k + 1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[k-1], fib[k])
