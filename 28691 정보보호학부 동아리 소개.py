# 동아리 이름을 매핑하는 딕셔너리
club_names = {
    'M': 'MatKor',
    'W': 'WiCys', 
    'C': 'CyKor',
    'A': 'AlKor',
    '$': '$clear'
}

# 입력받은 첫 글자로 동아리 이름 찾기
first_letter = input()
print(club_names[first_letter])