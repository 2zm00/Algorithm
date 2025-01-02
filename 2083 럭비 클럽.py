while True:
    # 입력 받기
    data = input().split()
    
    # 종료 조건 확인
    if data[0] == '#':
        break
        
    # 입력값 파싱
    name = data[0]
    age = int(data[1])
    weight = int(data[2])
    
    # 성인부/청소년부 분류
    if age > 17 or weight >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")
