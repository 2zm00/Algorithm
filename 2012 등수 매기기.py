n = int(input())
expected = []
for _ in range(n):
	expected.append(int(input()))

expected.sort()

result = 0
for i in range(n):
	result += abs(expected[i] - (i + 1))

print(result)
