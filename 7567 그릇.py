def calculate_height(dishes):
    height = 10  # 첫 번째 그릇의 높이
    for i in range(1, len(dishes)):
        if dishes[i] == dishes[i - 1]:
            height += 5  # 같은 방향으로 포개진 경우
        else:
            height += 10  # 반대 방향으로 포개진 경우
    return height

# 입력 받기
dishes = input()
# 결과 출력
print(calculate_height(dishes))
