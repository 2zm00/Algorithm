n , k = map(int, input().split())
children = list(map(int, input().split()))

differences = []
for i in range(1, n):
    differences.append(children[i] - children[i-1])

# 키 차이를 내림차순으로 정렬
differences.sort(reverse=True)

# 가장 큰 K-1개의 차이 제외 후 합 계산
result = sum(differences[k-1:])

print(result)