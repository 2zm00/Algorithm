# 익은 토마토 상하좌우로 영향을 받아 익게 됨
# 대각선은 영향을 주지 못하고 저절로 익는경우도 없음
# 며칠이 지나야 다 익게 되는지 (다 퍼져나가는지)

# M가로 N세로
# 둘째 줄 부터 N까지 maps 전달함
# 1 익은 0 익지않은 -1 없는

# 보통 : 익을 때 까지 최소 날짜
# 처음부터 모든 게 익어있으면 : 0
# 모두 익지못하는 상황이면 -1
from collections import deque

# 입력받아주기
m, n = map(int, input().split())
# 지도를 보여주니까 지도를 담을 빈 리스트 뚫기
maps = []



# 며칠인지 설정하기
res =0 
# 빈 큐 만들기
q = deque()

# 방향설정하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

	

# 지도 입력받기 + 토마토 익는 거 빈 큐에 추가하기
for i in range(n):
	temp_map = list(map(int,input().split()))
	maps.append(temp_map)
	for j in range(m):
		if maps[i][j] == 1:
			q.append((i,j))


def bfs():
	
	while q:
		# 현재 익은 토마토 위치
		x, y = q.popleft()
		for i in range(4):

			# 상자 범위 내의 있고 익지 않은 토마토라면?
			nx, ny = dx[i]+x, dy[i]+y
			if 0<= nx< n and 0 <= ny < m and maps[nx][ny] == 0:
				# 익은 날짜 +1
				maps[nx][ny] = maps[x][y] + 1
				q.append((nx, ny))


bfs()

for i in range(n):
	for j in range(m):
		if maps[i][j] == 0:
			print(-1)
			exit()
		if maps[i][j] > res:
			res = maps[i][j]

print(res -1)

