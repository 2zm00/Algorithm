import sys

# 입력 속도 개선을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 상근이가 가지고 있는 숫자 카드의 개수 N
n = int(input())
# 상근이가 가지고 있는 숫자 카드 목록 (set으로 저장하여 탐색 시간 단축)
# set의 in 연산은 평균적으로 O(1) 시간 복잡도를 가짐
sang_cards = set(map(int, input().split()))

# 확인할 숫자의 개수 M
m = int(input())
# 확인할 숫자 목록
check_nums = list(map(int, input().split()))

# 결과를 저장할 리스트
results = []

# 확인할 각 숫자에 대해 반복
for num in check_nums:
    # 해당 숫자가 상근이의 카드 목록(set)에 있는지 확인
    if num in sang_cards:
        results.append(1) # 있으면 1 추가
    else:
        results.append(0) # 없으면 0 추가

# 결과 리스트의 요소들을 공백으로 구분하여 출력
# print(*리스트)는 리스트의 요소들을 언패킹하여 개별 인자로 전달
print(*results)
