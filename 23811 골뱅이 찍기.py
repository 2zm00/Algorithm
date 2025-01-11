def print_snail_shape(N):
    # 상단 가로줄
    for _ in range(N):
        print('@' * (5 * N))
    
    # 첫 번째 세로줄
    for _ in range(N):
        print('@' * N)
    
    # 중간 가로줄
    for _ in range(N):
        print('@' * (5 * N))
    
    # 두 번째 세로줄
    for _ in range(N):
        print('@' * N)
    
    # 하단 가로줄
    for _ in range(N):
        print('@' * (5 * N))

# 입력 받기
N = int(input())
print_snail_shape(N)
