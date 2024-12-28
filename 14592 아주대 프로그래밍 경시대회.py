def rank_participants(N, participants):
    # 참가자 정보를 점수(내림차순), 제출 횟수(오름차순), 업로드 시간(오름차순)으로 정렬
    sorted_participants = sorted(enumerate(participants, 1), 
                               key=lambda x: (-x[1][0], x[1][1], x[1][2]))
    # 1등의 번호 반환
    return sorted_participants[0][0]

# 입력 받기
N = int(input())
participants = []
for _ in range(N):
    S, C, L = map(int, input().split())
    participants.append((S, C, L))

# 결과 출력
print(rank_participants(N, participants))
