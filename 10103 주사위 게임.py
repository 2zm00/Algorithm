# 라운드 수 입력받기
n = int(input())

# 초기 점수 설정
chang = 100  # 창영이의 점수
sang = 100   # 상덕이의 점수

# n번의 라운드 진행
for _ in range(n):
    # 각 라운드의 주사위 값 입력받기
    c, s = map(int, input().split())
    
    # 주사위 값 비교
    if c < s:
        chang -= s  # 창영이가 졌을 때
    elif c > s:
        sang -= c   # 상덕이가 졌을 때
    # 같은 값이 나왔을 때는 아무도 점수를 잃지 않음

# 결과 출력
print(chang)
print(sang)