def divide_fruits(a, b):
    results = []
    for friends in range(1, min(a, b) + 1):
        if a % friends == 0 and b % friends == 0:
            results.append((friends, a // friends, b // friends))
    return results

# 입력 받기
a, b = map(int, input().split())

# 결과 계산 및 출력
results = divide_fruits(a, b)
for friends, apples, bananas in results:
    print(friends, apples, bananas)
