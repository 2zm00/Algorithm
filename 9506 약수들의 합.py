def is_perfect_number(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) == n, divisors

while True:
    n = int(input())
    if n == -1:
        break

    is_perfect, divisors = is_perfect_number(n)

    if is_perfect:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")
