def calculate_work_time(start, end):
    h1, m1, s1 = start
    h2, m2, s2 = end
    
    # 시, 분, 초 각각 계산
    s = s2 - s1
    m = m2 - m1
    h = h2 - h1
    
    # 초가 음수일 경우 처리
    if s < 0:
        s += 60
        m -= 1
    
    # 분이 음수일 경우 처리
    if m < 0:
        m += 60
        h -= 1
    
    return h, m, s

# 입력 처리
for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    h, m, s = calculate_work_time((h1, m1, s1), (h2, m2, s2))
    print(h, m, s)
