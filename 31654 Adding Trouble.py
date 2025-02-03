# 입력 받기
A, B, C = map(int, input().split())

# A + B가 C와 같은지 확인
if A + B == C:
    print("correct!")
else:
    print("wrong!")
