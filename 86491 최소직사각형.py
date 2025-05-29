def solution(sizes):
    sorted_sizes = []
    for arr in sizes:
        sorted_arr=sorted(arr)
        sorted_sizes.append(sorted_arr)
#     정렬은 완료, 이제 큰 수 작은 수 중 가장 큰 거 뽑기

    long_lengths = []
    short_lengths = []
    
    for arr in sorted_sizes:
        short_lengths.append(arr[0])
        long_lengths.append(arr[1])
        
    answer = max(short_lengths)*max(long_lengths)
    
    return answer

# 문제풀이
# 지갑의 크기를 반환해야함
# 1. 가로, 세로 들의 길이를 크기 순으로 정렬
# 2. 그 중 큰 수 중에서 가장 큰 수와 작은 수 중에서 가장 작은 수 뽑아냄
# 3. 그 수의 곱을 지갑의 크기로 하면 될 듯

# 2차원 배열 안에 있는 수를 정렬하는 방법
# 인덱스 0을 작은 수 1을 큰 수
# 작은 수 들 중 가장 큰 수 / 큰 수 들 중 가장 큰 수
# 곱

# sorted_sizes = []
# for arr in sizes:
#   sorted_arr = sorted(arr)
#   sorted_sizes.append(sorted_arr)

####### 제약조건
# 1 <= sizes <= 10000
# w 가로 h 세로
# 1 <= w, h <= 1000