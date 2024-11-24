import math

def largest_square_side_length(tiles):
    return int(math.sqrt(tiles))

# 입력값 테스트
n = int(input())
result = largest_square_side_length(n)
print(f'The largest square has side length {result}.')