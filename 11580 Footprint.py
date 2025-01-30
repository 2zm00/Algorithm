def count_unique_footprints(commands):
    # 시작 위치
    x, y = 0, 0
    visited = set()
    visited.add((x, y))  # 원점 추가

    # 이동 방향 정의
    moves = {
        'E': (1, 0),   # 동쪽: x+1
        'W': (-1, 0),  # 서쪽: x-1
        'S': (0, -1),  # 남쪽: y-1
        'N': (0, 1)    # 북쪽: y+1
    }

    # 각 명령어 처리
    for command in commands:
        dx, dy = moves[command]
        x += dx
        y += dy
        visited.add((x, y))

    # 유일한 발자국 개수 반환
    return len(visited)

# 입력 처리
L = int(input())
commands = input()

# 결과 출력
print(count_unique_footprints(commands))
