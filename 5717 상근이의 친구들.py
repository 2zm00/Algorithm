while True:
    # 남자 친구 수(M)와 여자 친구 수(F) 입력 받기
    M, F = map(int, input().split())
    
    # 입력이 0 0이면 종료
    if M == 0 and F == 0:
        break
    
    # 총 친구 수 계산 및 출력
    total = M + F
    print(total)