import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 1. 입력 받기
N = int(input().strip())
coords = list(map(int, input().strip().split()))

# 2. 중복 제거 및 정렬
# set을 사용하여 중복을 제거하고 sorted()로 정렬
sorted_unique_coords = sorted(list(set(coords))) # set은 정렬되지 않으므로 list로 변환 후 정렬

# 3. 값-순위 매핑 생성 (딕셔너리 사용)
# {좌표값: 순위(0부터 시작)} 형태의 딕셔너리 생성
coord_to_rank = {value: idx for idx, value in enumerate(sorted_unique_coords)}
# enumerate는 (인덱스, 값) 튜플을 반환하므로 이를 이용해 딕셔너리를 쉽게 만들 수 있음

# 4. 좌표 변환
# 원래 좌표 리스트를 순회하며 딕셔너리에서 해당 값의 순위(압축된 좌표)를 찾음
compressed_coords = [coord_to_rank[value] for value in coords]

# 5. 출력
# map(str, ...)을 사용하여 리스트의 모든 요소를 문자열로 변환 후 ' '.join으로 공백 구분 출력
print(' '.join(map(str, compressed_coords)))

