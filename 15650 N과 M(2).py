import sys
input = sys.stdin.readline

def dfs(start, sequence):
    # sequence의 길이가 M과 같으면 출력한다.
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    # start부터 N까지 반복하여 숫자를 선택
    for i in range(start, N + 1):
        sequence.append(i)      # 현재 숫자 추가
        dfs(i + 1, sequence)      # 다음 숫자는 i+1부터 선택 (오름차순 유지)
        sequence.pop()          # 백트래킹: 마지막 숫자 제거

# 입력 받기
N, M = map(int, input().strip().split())
dfs(1, [])
