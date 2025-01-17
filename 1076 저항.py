# 색상별 값과 곱수를 딕셔너리로 정의
color_values = {
    'black': (0, 1),
    'brown': (1, 10),
    'red': (2, 100),
    'orange': (3, 1000),
    'yellow': (4, 10000),
    'green': (5, 100000),
    'blue': (6, 1000000),
    'violet': (7, 10000000),
    'grey': (8, 100000000),
    'white': (9, 1000000000)
}

# 입력 받기
first = input()
second = input()
third = input()

# 저항값 계산
first_value = color_values[first][0]
second_value = color_values[second][0]
multiplier = color_values[third][1]

# 최종 저항값 계산
resistance = (first_value * 10 + second_value) * multiplier

# 결과 출력
print(resistance)
