# 최대한 비싸게 사서 카드갯수를 충족하는 카드팩을 사야함
# 꼭 카드팩들 카드 합은 N과 같아야함

import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

dp = [0]*(n+1)

# [0][0][0][0]..n개
# dp는 점화식 만드는 문제

dp[0]=0

# 힌트 썼음..

"""
n=5야
그럼 i=4일때 j=5(n)-4(i)=1 이어야 함 
그럼 i=3일때 j=5(n)-3(i)=2 이어야 함 

"""
for i in range(1, n+1):
	for j in range(1, i+1):
		dp[i] = max(dp[i], dp[i-j] + card[j-1])

print(dp[n])

