def find_pairs(n):
    pairs = []
    for i in range(1, n//2 + 1):  # i는 1부터 n의 절반까지
        j = n - i
        if j > i:  # j가 i보다 큰 경우만 포함
            pairs.append((i, j))
    return pairs

def format_output(n, pairs):
    if not pairs:
        return f"Pairs for {n}:"
    pair_str = ', '.join(f'{i} {j}' for i, j in pairs)
    return f"Pairs for {n}: {pair_str}"

# 입력 처리
case = int(input())
for _ in range(case):
    n = int(input())
    pairs = find_pairs(n)
    print(format_output(n, pairs))