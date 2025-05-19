from collections import deque

def solution(n, edge):
	graph = [[] for _ in range(n+1)]
	q = deque()
	q.append(1)

	visited = [-1]*(n+1)
	visited[1]=0

	for a, b in edge:
		graph[a].append(b)
		graph[b].append(a)

	while q:
		now = q.popleft()

		for node in graph[now]:
			if visited[node] == -1:
				visited[node] = visited[now]+ 1
				q.append(node)



	answer = visited.count(max(visited))

	return answer



# 가장 먼 노드가 몇 개인지 풀력

# n 개의 노드가 있는 그래프가 있음.
# 1~n 번호
# 1번 노드에서 가장 멀리 떨어진 노드 갯수 구하기
# 가장 멀리 = 최단경로 간선 갯수가 가장 많은 노드

# 2차원 배열의 vertex 매개변수