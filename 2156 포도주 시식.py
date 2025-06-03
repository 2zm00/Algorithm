# 포도주 선택하면 다 마시고 원래 위치로 놓아야함
# 연속 3잔을 모두 마실 수 없음 두잔까지만
# 1부터 n 번호 있고 최댓값 구하기

import sys
input = sys.stdin.readline

n = int(input())
# 포도주 잔 갯수 입력

wines = [int(input()) for _ in range(n)]

if n == 1:
	print(wines[0])
	sys.exit()

dp = [0] *n
dp[0] = wines[0] #첫잔 안마심
dp[1] = wines[0]+wines[1] #첫잔 마심


	

# 첫번째 포도주를 무조건 마셔야된다는 조건이 없으므로 구분해줘야댐
# 연속 2번까지 마시는거 허용이므로 이거까지 잡아주고

# 3잔째라면, 3+2+0 3+1+0  이니까
if n>=3:
	dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])
	for i in range(3, n):
		dp[i] = max(wines[i]+wines[i-1]+dp[i-3], wines[i]+dp[i-2],dp[i-1])

print(dp[-1])
# 마지막잔도 조건이 없으므로 마신거 안마신 거 중 최대


# max(dp[i-1])인지 dp[i-2]인지 너무 헷갈림