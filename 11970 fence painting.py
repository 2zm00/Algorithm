def total_painted_length(a, b, c, d):
    # 두 구간의 전체 길이를 계산
    length1 = b - a
    length2 = d - c
    
    # 겹치는 구간 계산
    overlap_start = max(a, c)
    overlap_end = min(b, d)
    overlap = max(0, overlap_end - overlap_start)
    
    # 전체 칠해진 길이 = 두 구간의 길이 합 - 겹치는 길이
    return length1 + length2 - overlap

# 입력 받기
a, b = map(int, input().split())
c, d = map(int, input().split())

# 결과 출력
print(total_painted_length(a, b, c, d))
