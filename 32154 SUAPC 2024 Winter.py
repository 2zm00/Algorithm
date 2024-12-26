def get_team_info(N):
    # 스코어보드 데이터 딕셔너리
    scoreboard = {
        1: (11, 'A B C D E F G H J L M'),
        2: (9, 'A C E F G H I L M'),
        3: (9, 'A C E F G H I L M'),
        4: (9, 'A B C E F G H L M'),
        5: (8, 'A C E F G H L M'),
        6: (8, 'A C E F G H L M'),
        7: (8, 'A C E F G H L M'),
        8: (8, 'A C E F G H L M'),
        9: (8, 'A C E F G H L M'),
        10: (8, 'A B C F G H L M')
    }
    
    # N등 팀의 정보 반환
    return scoreboard[N]

# 입력 받기
N = int(input())

# 결과 출력
problems_solved, problem_list = get_team_info(N)
print(problems_solved)
print(problem_list)