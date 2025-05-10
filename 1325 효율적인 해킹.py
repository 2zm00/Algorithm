from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)

# B -> A로 탐색하는 간선을 선택해야함

# [0] [0] [0] [1] [0] [0]
# [0] [0] [0] [1] [0] [0]
# [0] [1] [1] [0] [1] [1]
# [0] [0] [0] [0] [0] [0]
# [0] [0] [0] [0] [0] [0]

def bfs(start_node, n ,graph):
	q = deque()
	q.append(start_node)

	visited = [False] * (n+1)
	visited[start_node] = True

	hacked_count = 1

	while q :
		current = q.popleft()
		for next_node in graph[current]:
			if not visited[next_node]:
				visited[next_node]=True
				q.append(next_node)
				hacked_count += 1
	return hacked_count

max_hacked=0
result_computer=[]

for i in range(1, n+1):
	current_hacked_count = bfs(i, n ,graph)
	if current_hacked_count > max_hacked:
		max_hacked = current_hacked_count
		result_computer = [i]
	elif current_hacked_count == max_hacked:
		result_computer.append(i)	

result_computer.sort()
print(*result_computer)