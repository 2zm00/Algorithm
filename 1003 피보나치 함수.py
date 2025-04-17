def main():
    import sys
    input = sys.stdin.read().split()  # 모든 입력 한 번에 읽기
    
    max_n = 40
    zero = [0] * (max_n + 1)  # 0~40 인덱스 사용
    one = [0] * (max_n + 1)
    
    # 초기 조건 설정
    zero[0] = 1  # fib(0)에서 0 출력 1회
    one[1] = 1   # fib(1)에서 1 출력 1회
    
    # DP 테이블 채우기
    for i in range(2, max_n + 1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]
    
    # 테스트 케이스 처리
    T = int(input[0])
    for n in map(int, input[1:T+1]):  # 첫 번째 값은 T, 이후는 테스트 케이스
        print(f"{zero[n]} {one[n]}")

if __name__ == "__main__":
    main()
