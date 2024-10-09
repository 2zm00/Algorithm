def generate_integer_type(n):
    if n % 4 != 0 or n < 4 or n > 1000:
        raise ValueError('N must be a multiple of 4 and between 4 and 1000.')
    base_type = 'long'
    count = n // 4
    return ' '.join([base_type] * count + ['int'])


n = int(input())
print(generate_integer_type(n))