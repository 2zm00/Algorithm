import sys
input = sys.stdin.readline

N, M =map(int, input().split())
numbers = sorted(map(int, input().split()))
lst = []


def dfs(start):
	if len(lst) == M:
		print(" ".join(map(str, lst)))
		return
	
	for i in range(start,N):
		lst.append(numbers[i])
		dfs(i+1)
		lst.pop()

dfs(0)
