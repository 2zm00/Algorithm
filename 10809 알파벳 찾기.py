S = input().strip()

# 각 알파벳의 첫 등장 위치를 저장할 리스트 초기화 (-1로 설정)
result = [-1] * 26

# 문자열을 순회하며 첫 등장 위치 기록
for i in range(len(S)):
    alphabet_index = ord(S[i]) - ord('a')
    if result[alphabet_index] == -1:
        result[alphabet_index] = i

# 결과를 공백으로 구분하여 출력
print(' '.join(map(str, result)))
