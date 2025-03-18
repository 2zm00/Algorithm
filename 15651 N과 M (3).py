import sys
input = sys.stdin.readline

# 함수 정의
def dfs(start, depth):

	# depth의 길이가 M과 같으면 출력하고 함수 종료 [종료조건]
	if len(depth)==M:
		print(" ".join(map(str, depth)))
		return

	# start부터 N까지 반복하여 숫자를 선택 [시작조건]
	for i in range(start, N+1):
		depth.append(i)
		dfs(i+1, depth)
		# backtracking: depth에서 마지막 문자를 제거
		depth.pop()

# 입력받기
N, M = map(int, input().split())
# dfs 함수 호출, 시작 숫자는 1, depth는 빈 리스트
dfs(1, [])
