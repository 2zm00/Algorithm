
# 집이 N개 거리는 선분
# 빨파초 중 하나 칠해야함
# 각 색별로 비용이 다름
# 모든집 칠하는 비용 최솟값
# 이전 집과 색이 달라야함

# 첫 줄 집 수 N
# 2줄 빨 초 파  1번집 비용
# 3줄 빨 초 파 2번집 비용
# N+1줄 빨 초 파 N번집 비용

import sys
input = sys.stdin.readline

n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
# dp 값 초기화
# dp[비용][0빨 1초 2파]
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

# 셋 중 최솟값이어야 하나? 근데 조합했을 때 가장 싼거여야하니까 그냥 0으로 초기화시켜야될듯

for i in range(1,n):
	# dp[i]의 현재는 3개 중에 최소로 골랐을 때 시나리오 3개를 다 보고 빨 초 파 고른거 중복 방지시켜야함
	dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
	dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
	dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
