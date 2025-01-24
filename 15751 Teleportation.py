def minimum_distance(a, b, x, y):
    # 직접 운반하는 거리
    direct_distance = abs(a - b)
    
    # 텔레포터를 이용하는 거리
    # 1) a -> x -> y -> b 또는
    # 2) a -> y -> x -> b 중 최소값
    via_teleporter = min(abs(a - x) + abs(b - y), abs(a - y) + abs(b - x))
    
    # 두 방법 중 최소값 반환
    return min(direct_distance, via_teleporter)

# 입력 받기
a, b, x, y = map(int, input().split())

# 결과 출력
print(minimum_distance(a, b, x, y))
