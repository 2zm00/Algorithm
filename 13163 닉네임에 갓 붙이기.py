# 닉네임 수 입력받기
n = int(input())

# n개의 닉네임 입력받기
nicknames = []
for _ in range(n):
    nicknames.append(input())

# 닉네임 변환 함수
def add_god_to_nicknames(nicknames):
    result = []
    for nickname in nicknames:
        # 공백으로 음절 분리
        syllables = nickname.split()
        # 첫 음절을 'god'으로 바꾸고 나머지 음절 연결
        if syllables:
            new_name = 'god' + ''.join(syllables[1:])
            result.append(new_name)
    return result

# 변환된 닉네임 출력
result = add_god_to_nicknames(nicknames)
for name in result:
    print(name)
