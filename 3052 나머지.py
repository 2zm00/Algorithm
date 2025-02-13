remainders = []
for _ in range(10):
    num = int(input())
    remainders.append(num % 42)
print(len(set(remainders)))
