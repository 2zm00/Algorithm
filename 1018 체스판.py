N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_repaint = float('inf')


for i in range(N - 7):
    for j in range(M - 7):
        white_start = 0
        black_start = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':
                        white_start += 1
                    if board[i + x][j + y] != 'B':
                        black_start += 1
                else:
                    if board[i + x][j + y] != 'B':
                        white_start += 1
                    if board[i + x][j + y] != 'W':
                        black_start += 1
        min_repaint = min(min_repaint, white_start, black_start)

print(min_repaint)