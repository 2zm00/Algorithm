# 입력 받기
n = int(input())  # 테스트 케이스 개수

# 결과 저장 리스트
results = []

for _ in range(n):
    p = int(input())  # 선수의 수
    max_price = 0
    max_player = ""
    
    for _ in range(p):
        # 선수 정보 입력 받기
        c, name = input().split(maxsplit=1)
        c = int(c)  # 가격을 정수로 변환
        
        # 가장 비싼 선수 찾기
        if c > max_price:
            max_price = c
            max_player = name
    
    # 결과 저장
    results.append(max_player)

# 결과 출력
for result in results:
    print(result)
