import sys
input = sys.stdin.readline

n = int(input())





def solve(n):
	dp = [0]*(n+1)
	if n ==0 :
		return 1
	if n >= 0 :
		dp[0]= 1
	if n >=1:
		dp[1]=1
	if n >= 2:
		dp[2]=2
	if n >=3 :
		dp[3]=4

	for i in range(4,n+1):
		dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
	return dp[n]

results = []

for _ in range(n):
	n = int(input())
	results.append(solve(n))

for res in results:
	print(res)
