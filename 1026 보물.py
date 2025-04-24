n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

result = 0

for i in range(n):
	result += a[i] * b[i]

print(result)


# 풀이과정
# 1. a, b를 리스트에 담는다
# 2. a는 내림차순으로 정렬하고 b는 오름차순으로 정렬한다 (최솟값을 구하기 위해선 큰거*작은거 를 해야하기 때문)
# 3. result에 a[i] * b[i]를 더해준다
# 4. result를 출력한다