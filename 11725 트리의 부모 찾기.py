import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)



visited = [False]*(n+1)

def dfs(node):
	for i in graph[node]:
		if visited[i]== False:
			visited[i]=node
			dfs(i)

dfs(1)

for x in range(2,n+1):
	print(visited[x])


# 언제 setrecursionlimit을 설정해야하는거야?
"""
RecursionError는 재귀와 관련된 에러이다.

파이썬이 기본으로 제공하는 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발상한다.

sys.getrecursionlimit()을 이용해 파이썬이 제공하는 재귀 깊이를 알 수 있고, 이 값은 1000으로 되어 있다.


"""