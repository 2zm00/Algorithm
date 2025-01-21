# 약칭과 정식 명칭을 매핑하는 딕셔너리 생성
school_names = {
    "NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy"
}

# 입력 받기
abbreviation = input()

# 정식 명칭 출력
print(school_names[abbreviation])
