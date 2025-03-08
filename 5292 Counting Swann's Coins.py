def count_coins(n):
    result = []
    group = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            group.append("DeadMan")
        elif i % 3 == 0:
            group.append("Dead")
        elif i % 5 == 0:
            group.append("Man")
        else:
            group.append(str(i))
        
        # 그룹을 새 줄로 출력
        if len(group) > 0 and (i % 3 == 0 or i % 5 == 0): 
            result.append(" ".join(group))
            group = []

    # 남아 있는 숫자 출력
    if group:
        result.append(" ".join(group))
    
    # 결과 출력
    print("\n".join(result))

# 테스트 실행
n = int(input())
count_coins(n)
