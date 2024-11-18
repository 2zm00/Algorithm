def translate_russian_like(word):
    translations = {
        'A': 'a', 'K': 'k', 'M': 'm', 'O': 'o', 'T': 't',
        'B': 'v', 'E': 'ye', 'H': 'n', 'P': 'r',
        'C': 's', 'Y': 'u', 'X': 'h',
    }
    return ''.join(translations.get(char, '') for char in word)

# 입력 받기
word = input()
# 결과 출력
print(translate_russian_like(word))