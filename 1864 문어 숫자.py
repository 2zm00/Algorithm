# 문어 숫자와 대응하는 값 매핑
octopus_map = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}

def octopus_to_decimal(octopus_number):
    decimal_value = 0
    length = len(octopus_number)
    
    # 오른쪽에서 왼쪽으로 처리하며 계산
    for i, char in enumerate(octopus_number):
        power = length - i - 1
        decimal_value += octopus_map[char] * (8 ** power)
    
    return decimal_value

# 입력 처리 및 출력
while True:
    octopus_number = input().strip()
    if octopus_number == '#':
        break
    print(octopus_to_decimal(octopus_number))
