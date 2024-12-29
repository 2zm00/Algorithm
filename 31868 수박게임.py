def max_watermelons(N, K):
    # K개의 체리로 만들 수 있는 2단계 과일의 개수
    level2 = K // 2
    
    # 남은 체리는 사용할 수 없음
    remaining = level2
    
    # 3단계부터 N단계까지 반복
    for i in range(3, N + 1):
        # 현재 단계에서 만들 수 있는 과일의 개수
        remaining = remaining // 2
    
    return remaining

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(max_watermelons(N, K))