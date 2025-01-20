def is_problem_easy(s1, s2):
    # s1이 s2의 절반 이상인지 확인
    if s1 >= s2 / 2:
        return "E"
    else:
        return "H"

# 입력 받기
s1, s2 = map(int, input().split())
print(is_problem_easy(s1, s2))
