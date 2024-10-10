def fibo2(n, memo={}):
	if n <= 1 :
		return n
	if n in memo:
		return memo[n]
	memo[n] = fibo2(n-1,memo)+fibo2(n-2,memo)
	return memo[n]

n= int(input())
print(fibo2(n))