def solve():
    P = int(input())
    for _ in range(P):
        N, D, A, B, F = map(float, input().split())
        # 두 기차가 충돌할 때까지 걸리는 시간 계산
        time = D / (A + B)
        # 파리가 이동한 총 거리 계산
        distance = F * time
        # 결과 출력 (소수점 6자리까지)
        print(f"{int(N)} {distance:.6f}")

solve()
