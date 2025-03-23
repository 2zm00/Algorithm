import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(map(int, input().split()))
lst = []

def dfs(start, depth):
	if len(depth) == M:
		print(" ".join(map(str, lst)))
		return
	
	for i in range(start, N+1):
		lst.append(num[i])
		dfs(i+1)
		lst.pop()

dfs(0)