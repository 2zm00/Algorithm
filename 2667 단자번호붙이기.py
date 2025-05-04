from collections import deque

n = int(input())

maps = []
result = []

for _ in range(n):
	maps.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a,b):
	queue = deque()
	queue.append((a,b))
	maps[a][b]=0
	count = 1

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= n:
				continue
			if maps[nx][ny] ==1:
				maps[nx][ny] = 0
				queue.append((nx,ny))
				count += 1
	return count
# count에는 집의 크기

# result에는 집의 갯수
for i in range(n):
	for j in range(n):
		if maps[i][j]==1:
			result.append(bfs(i,j))

result.sort()

print(len(result))
for num in result:
	print(num)
