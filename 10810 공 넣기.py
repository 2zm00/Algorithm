n, m = map(int, input().split())
baskets = [0] * (n + 1)  # 바구니 1~n번 사용

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        baskets[idx] = k

print(' '.join(map(str, baskets[1:n+1])))
