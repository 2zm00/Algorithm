# n 종류 동전
# 가치의 합 k원 되게 하는데 동전 갯수가 최소
# 불가능 -1 (불가능이 있을 수 있다는 소리)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [float('inf')]*(k+1)
dp[0]=0
# 무한대로 해서 동전갯수 무한 개 썼다
# dp에 뭘 담아야하지?
# dp에 동전 갯수

# 15원 까지 1원 15개, 5원 3개, 12원1개 1원3개 = 4개
"""
3 17
11
5
13


i는 2부터 15까지

dp[0] = 무한개
dp[2] = min(dp[2], dp[0]+1) = 1
dp[3] = min(dp[3], dp[2]=1 + 1 =2) =2 ? 근데 cost안에 없으므로 -1
dp[4] = min(dp[4], dp[3]=2+1 =3)
dp[5] = cost[1]*1 = 1
dp[5] = cost[0]*5 = 5
dp[15] = cost[0]*15 = 15
dp[]
"""

# 너무 가격 없는거 까지 배열 만들면 안되니까 가격 있는 걸로다가 시작점 잡으면 되지않을까?
for coin in coins:
	for i in range(coin,k+1):
		dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == float('inf'):
	print(-1)
else: 
	print(dp[k])