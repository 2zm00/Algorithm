# 알파벳별 다이얼 시간 매핑
letter_to_time = {
    'A': 3, 'B': 3, 'C': 3,   # 2 + 1
    'D': 4, 'E': 4, 'F': 4,   # 3 + 1
    'G': 5, 'H': 5, 'I': 5,   # 4 + 1
    'J': 6, 'K': 6, 'L': 6,   # 5 + 1
    'M': 7, 'N': 7, 'O': 7,   # 6 + 1
    'P': 8, 'Q': 8, 'R': 8, 'S': 8,  # 7 + 1
    'T': 9, 'U': 9, 'V': 9,   # 8 + 1
    'W': 10, 'X': 10, 'Y': 10, 'Z': 10 # 9 + 1
}

# 입력받은 단어의 최소 다이얼 시간을 계산하는 함수
def minimum_dial_time(word):
    return sum(letter_to_time[char] for char in word)

# 입력 받기
word = input().strip()

# 결과 출력
print(minimum_dial_time(word))