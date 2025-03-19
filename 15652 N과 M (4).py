import sys
input = sys.stdin.readline

# 함수정의
def dfs(start, depth):
	# 종료 지점 설정
	# 만약 깊이가 M과 같다면
	if len(depth)==M:
		# 출력하고 종료
		print(" ".join(map(str, depth)))
		return
	
	# 시작 지점 설정
	# 1부터 N+1까지 반복
	for i in range(start, N+1):
		# 빈 리스트에 i 추가
		depth.append(i)
		# 재귀함수 호출해서 1대신 i로 넣어주고, 깊이도 넣어줌
		dfs(i, depth)
		# backtracking: i를 depth에서 제거
		depth.pop()	

N, M = map(int, input().split())
dfs(1, [])

'''
N, M = 3, 3

dfs(1, [])
# i는 1부터 3까지 순회
i = 1
depth.append(1)
depth = [1]
dfs(1, [1])  # start = 1, depth = [1]
	# i는 1부터 3까지 순회
	i = 1
	depth.append(1)
	depth = [1, 1]
	dfs(1, [1, 1])  # start = 1, depth = [1, 1]
	# i는 1부터 3까지 순회
	i = 1
	depth.append(1)
	depth = [1, 1, 1]
	dfs(1, [1, 1, 1])  # start = 1, depth = [1, 1, 1]
		# len(depth) == M 이므로 출력 후 종료
		print("1 1 1")
	depth.pop()  # depth = [1, 1]
	
	i = 2
	depth.append(2)
	depth = [1, 1, 2]
	dfs(2, [1, 1, 2])  # start = 2, depth = [1, 1, 2]
		# len(depth) == M 이므로 출력 후 종료
		print("1 1 2")
	depth.pop()  # depth = [1, 1]

	i = 3
	depth.append(3)
	depth = [1, 1, 3]
	dfs(3, [1, 1, 3])  # start = 3, depth = [1, 1, 3]
		# len(depth) == M 이므로 출력 후 종료
		print("1 1 3")
	depth.pop()  # depth = [1, 1]

	# dfs(1, [1, 1])의 for문 종료
	depth.pop()  # depth = [1]

	i = 2
	depth.append(2)
	depth = [1, 2]
	dfs(2, [1, 2])  # start = 2, depth = [1, 2]
	# i는 2부터 3까지 순회
	i = 2
	depth.append(2)
	depth = [1, 2, 2]
	dfs(2, [1, 2, 2])  # start = 2, depth = [1, 2, 2]
		print("1 2 2")
	depth.pop()

	i = 3
	depth.append(3)
	depth = [1, 2, 3]
	dfs(3, [1, 2, 3])  # start = 3, depth = [1, 2, 3]
		print("1 2 3")
	depth.pop()
	
	# dfs(1, [1])의 for문 종료
	depth.pop()

	i = 3
	depth.append(3)
	depth = [1, 3]
	dfs(3, [1, 3])  # start = 3, depth = [1, 3]
	# i는 3부터 3까지 순회
	i = 3
	depth.append(3)
	depth = [1, 3, 3]
	dfs(3, [1, 3, 3])  # start = 3, depth = [1, 3, 3]
		print("1 3 3")
	depth.pop()
	
	# dfs(1, [])의 for문 종료
	depth.pop()

'''