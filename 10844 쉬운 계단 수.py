# 인접한 모든 자리의 차이가 1을 계단 수
# 길이가 N 자릿수인 계단 수가 몇개인지 구해보기
# 0은 계단에 포함 안됨

# 1 2 3 4 5 6 7 8 9 = 9개
# 12 23 34 45 56 67 78 89 = 8개
# 10 21 32 43 54 65 76 87 98 = 9개라서 17

# n=3일때
# 101 121 123 212 210 232 234 321 323 343 345
# 432 434 454 456 543 545 567 565 676 678 654 656 
# 765 767 789 787 876 878 987 989 =29


import sys
input = sys.stdin.readline

n = int(input())
d = 10**9
dp = [[0]*10 for _ in range(n+1)]

"""
[0]|[   ][   ][   ][   ][   ][   ][   ][   ]|[9]
[0]|[   ][   ][ j ][   ][   ][   ][   ][   ]|[9]
[0]|[   ][j-1][   ][j+1][   ][   ][   ][   ]|[9]


0일때 1로 밖에 못감
9일때 9로 밖에 못감

j는 j-1 j+1로 밖에 못감
"""

for j in range(1,10):
	dp[1][j]=1

for i in range(2, n+1):
	for j in range(10):
		if j==0:
			dp[i][j] = (dp[i-1][1])%d
		elif j==9:
			dp[i][j] = (dp[i-1][8])%d
		else:
			dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%d

print(sum(dp[n])%d)