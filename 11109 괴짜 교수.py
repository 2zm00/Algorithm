T = int(input())  # 테스트 케이스 수

for _ in range(T):
    d, n, s, p = map(int, input().split())
    
    # 직렬 버전 총 시간: n * s
    serial_time = n * s
    
    # 병렬 버전 총 시간: d + (n * p)
    parallel_time = d + (n * p)
    
    if serial_time < parallel_time:
        print("do not parallelize")
    elif serial_time > parallel_time:
        print("parallelize")
    else:
        print("does not matter")