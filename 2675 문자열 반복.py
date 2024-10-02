# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # 반복 횟수 R과 문자열 S 입력
    R, S = input().split()
    R = int(R)
    
    # 새로운 문자열 P 생성
    P = ''
    for char in S:
        P += char * R
    
    # 결과 출력
    print(P)