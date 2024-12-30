def count_empty_slots(N, Q, instructions):
    # 슬롯 초기화 (0: 비어있음)
    slots = [0] * N
    
    # 각 명령어에 대해 풍선 설치
    for L, I in instructions:
        # L번 슬롯부터 I개씩 띄어가며 풍선 설치
        for i in range(L-1, N, I):
            slots[i] = 1  # 풍선 설치
    
    # 비어있는 슬롯(0) 개수 반환
    return slots.count(0)

# 입력 받기
N, Q = map(int, input().split())
instructions = []
for _ in range(Q):
    L, I = map(int, input().split())
    instructions.append((L, I))

# 결과 출력
print(count_empty_slots(N, Q, instructions))
