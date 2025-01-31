def check_string_parity(s):
    # 각 문자의 등장 횟수를 저장하는 딕셔너리
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # 모든 문자가 짝수 번 등장하는지 확인
    if all(count % 2 == 0 for count in char_counts.values()):
        return 0
    
    # 모든 문자가 홀수 번 등장하는지 확인
    if all(count % 2 == 1 for count in char_counts.values()):
        return 1
    
    # 위 조건에 해당하지 않는 경우
    return 2

# 입력 받기
s = input().strip()
# 결과 출력
print(check_string_parity(s))
