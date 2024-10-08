def fibo(n, mem={}):
	if n in mem:
		return mem[n]
	if n <= 1:
		return n
	mem[n] = fibo(n-1, mem) + fibo(n-2, mem)
	return mem[n]


n= int(input())
print(fibo(n))
