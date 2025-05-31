# 이번에는 최솟값 구하기

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp=[max(cards)]*(n+1)
dp[0]=0

"""
10
1 1 2 3 5 8 13 21 34 55
dp[1] = 1 한장살때 1원
dp[2] = min(dp[1]=1+card[0]=1 =2, card[1]=1) =1 두장살때 1원
i=3 j=2, dp[3] = min(dp[2]=1+card[0]=1 =2 3장, card[2]=1 3장2원) =2
i=4 j=1, dp[4] = min(dp[3]=2 (3장) + card1])
"""



	# 0임시 제외 n개 뚫어주기
for i in range(1,n+1):
	for j in range(1, i+1):
		if j <= len(cards): #이걸로 인덱스 음수로 넘어가는거 방지
			dp[i] = min(dp[i], dp[i - j] + cards[j - 1])

# n=10 i=7 j=6 // dp[7] = min(dp[7]=40, dp[1]+cards[5]=52)

print(dp[n])