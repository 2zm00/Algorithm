

# 사용자로부터 정수 N 입력 받기
N = int(input())



def fac(N):
    if N == 0:  # 0!은 1이므로 예외 처리
        return 1
    else:
        result = 1
        for i in range(1, N + 1):
            result *= i
        return result
    
    
# 팩토리얼 계산 및 출력
print(fac(N))