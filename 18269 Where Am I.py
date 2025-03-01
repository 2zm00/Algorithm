# 입력 받기
N = int(input().strip())
mailboxes = input().strip()

# K를 1부터 N까지 하나씩 증가시키며 검사
for k in range(1, N + 1):
    seen = set()  # 이미 본 k 길이의 문자열을 저장할 집합
    unique = True  # 현재 k의 모든 부분 문자열이 유일한지 확인하는 플래그
    for i in range(N - k + 1):
        substring = mailboxes[i:i+k]
        if substring in seen:
            unique = False
            break  # 중복이 있으므로 더 이상 검사할 필요 없음
        seen.add(substring)
    # 모든 k 길이의 부분 문자열이 중복 없이 유일하면, 결과 출력 후 종료
    if unique:
        print(k)
        break
