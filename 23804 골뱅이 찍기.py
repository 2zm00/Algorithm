def print_golbang(N):
    # 상단 부분 출력
    for _ in range(N):
        print('@' * (5 * N))
    
    # 중간 부분 출력
    for _ in range(3 * N):
        print('@' * N)
    
    # 하단 부분 출력
    for _ in range(N):
        print('@' * (5 * N))

N = int(input())
print_golbang(N)