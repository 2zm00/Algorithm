import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(map(int, input().split()))
lst = []

def dfs():
	if len(lst) == M:
		print(" ".join(map(str, lst)))
		return
	
	for i in num:
		lst.append(i)
		dfs()
		lst.pop()

dfs()