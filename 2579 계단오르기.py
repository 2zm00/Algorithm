# 계단오르기 규칙, 한번에 한계단/두계단 오를 수 있음
# 연속 3계단 안됨 (시작점 포함 안됨)
# 마지막 도착은 반드시 밟아야함

# 총 점수의 최댓값 구하기

stair_count = int(input())

# 첫번째 계단과 마지막 계단은 무조건 밟아야함

# 최대 하나만 건너뛸 수 있음 + 연속 3계단 안됨
dp = [[0]*2 for _ in range(stair_count+1)]
stair = []

for _ in range(stair_count):
	stair.append(int(input()))

dp[1][0] = stair[0]




for i in range(2, stair_count+1):
	dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stair[i-1]
	dp[i][1] = dp[i-1][0] + stair[i-1]

print(max(dp[stair_count][1], dp[stair_count][0]))
# 근데 마지막 계단을 밟아야하잖아..
# # dp[몇번째 계단][이전 계단을 밟았나(연속3계단 방지)] = 점수
# 왜 자꾸 예시를 넣으면 35가 나오지?