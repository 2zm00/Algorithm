from collections import deque

m, n, k = map(int, input().split())
maps = [[0] * n for _ in range(m)]

# 직사각형 영역 1로 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            maps[i][j] = 1

visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1  # 시작점도 영역에 포함되므로 1부터 시작

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count

areas = []
count = 0

for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 and not visited[i][j]:
            area = bfs(i, j, maps, visited)
            areas.append(area)
            count += 1

print(count)
print(*sorted(areas))
