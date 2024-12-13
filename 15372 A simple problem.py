import sys
input = sys.stdin.readline

# 테스트 케이스의 수 입력받기
T = int(input())

# 결과를 한번에 저장했다가 출력
answer = []
for _ in range(T):
    N = int(input())
    answer.append(N * N)

# 결과 한번에 출력
print('\n'.join(map(str, answer)))
