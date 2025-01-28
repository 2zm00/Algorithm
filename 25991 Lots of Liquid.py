def solve():
    # 입력 받기
    n = int(input())
    side_lengths = list(map(float, input().split()))
    
    # 총 부피 계산
    total_volume = sum(c ** 3 for c in side_lengths)
    
    # 새로운 큐브의 변의 길이 계산 (세제곱근)
    new_side_length = total_volume ** (1/3)
    
    # 결과 출력
    print(new_side_length)

solve()
