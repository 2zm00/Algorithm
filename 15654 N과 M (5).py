import sys
input = sys.stdin.readline

N, M =map(int, input().split())
num = sorted(map(int, input().split()))
# 주어진 수에 대해서만 수열을 해야되서 주어진 수를 담을 리스트 생성
lst = []
# 중복제거를 위한 visited boolean 리스트 생성
visited = [False]*N


def dfs(depth):
	if depth==M:
		print(" ".join(map(str, lst)))
		return

	for i in range(N):
		# 중복재거를 위해 visited에 True가 아닌 경우에만 탐색
		if not visited[i]:
			# 방문한 경우 True로 변경
			visited[i] = True
			lst.append(num[i])
			dfs(depth+1)
			# 다음 depth로 넘어가기 전에 방문한 것을 False로 변경
			visited[i] = False
			lst.pop()

dfs(0)

		