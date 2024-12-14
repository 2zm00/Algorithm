def calculate_student_id(scores):
    # 건물 번호 상수 정의
    humanities_building = 508
    international_building = 108
    engineering_building = 212
    itbt_building = 305
    haengwon_park = 707
    postal_code = 4763

    # 점수 할당
    korean, math, english, inquiry, second_language = scores

    # 첫 번째 구성요소 계산 (국어와 영어 비교)
    if korean > english:
        first_component = (korean - english) * humanities_building
    else:
        first_component = (english - korean) * international_building

    # 두 번째 구성요소 계산 (수학과 탐구 비교)
    if math > inquiry:
        second_component = (math - inquiry) * engineering_building
    else:
        second_component = (inquiry - math) * itbt_building

    # 세 번째 구성요소 계산 (제2외국어)
    third_component = second_language * haengwon_park

    # 최종 학번 계산
    student_id = (first_component + second_component + third_component) * postal_code

    return student_id

# 입력 처리
T = int(input())
scores = list(map(int, input().split()))

# 점수 리스트를 5개로 맞추기 (응시하지 않은 과목은 0점)
while len(scores) < 5:
    scores.append(0)

# 결과 출력
print(calculate_student_id(scores))
