def count_visible_trophies_from_left(heights):
    max_height = 0
    visible_count = 0
    for height in heights:
        if height > max_height:
            visible_count += 1
            max_height = height
    return visible_count

def count_visible_trophies_from_right(heights):
    max_height = 0
    visible_count = 0
    for height in reversed(heights):
        if height > max_height:
            visible_count += 1
            max_height = height
    return visible_count

# 입력 처리
N = int(input())
heights = [int(input()) for _ in range(N)]

# 결과 출력
print(count_visible_trophies_from_left(heights))
print(count_visible_trophies_from_right(heights))
