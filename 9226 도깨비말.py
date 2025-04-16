vowels = {'a', 'e', 'i', 'o', 'u'}

while True:
    word = input().strip()
    if word == '#':
        break
    index = 0
    # 첫 모음 위치 찾기
    for i, c in enumerate(word):
        if c in vowels:
            index = i
            break
    else:
        # 모음이 없는 경우
        index = len(word)
    # 변환된 단어 생성
    pig_latin = word[index:] + word[:index] + 'ay'
    print(pig_latin)
