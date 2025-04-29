# 수열 A 가 주어졌을 때 가장 긴 증가하는 부분 수열을 구해야하는 문제
# 수열 A 인 경우 가장 긴 증가하는 부분 수열은 {10, 20 30, 50} 이고 길이는 4


n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
	for j in range(i):
		if arr[j] < arr[i]:
			dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# dp는 리스트에 n만큼 1 씩으로 넣어주고
# 반복문을 거쳐서 i가 1일때, j가 0~i까지 가면서 arr[i]와 비교
# 즉, i 전까지 숫자들과 비교해서 i가 arr[j]<arr[i]를 만족하면 dp 배열안에 1씩 더해줌
# 그렇게 1 씩 더해져서 끝까지 가서 가장 큰 dp값이 최종 갯수이므로..