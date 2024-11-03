

def find_smallest_generator(N):
    for i in range(1, N):
        num_sum = i + sum(int(digit) for digit in str(i))
        if num_sum == N:
            return i
    return 0


N = int(input())
result = find_smallest_generator(N)
print(result)