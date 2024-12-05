a, b = input().split()
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

result = ''
for i in range(max_len):
    digit_sum = int(a[i]) + int(b[i])
    result += str(digit_sum)

print(int(result))