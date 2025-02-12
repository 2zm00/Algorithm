n, m = map(int, input().split())
baskets = list(range(n + 1))  # 인덱스 0은 무시

for _ in range(m):
    i, j = map(int, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

print(' '.join(map(str, baskets[1:])))
