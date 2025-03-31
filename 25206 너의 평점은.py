def calculate_grade_point_average():
    """전공평점을 계산하는 함수."""

    grade_map = {
        'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
    }

    total_credit_points = 0.0
    total_credits = 0.0

    for _ in range(20):
        try:
            subject, credit, grade = input().split()
            credit = float(credit)

            if grade != 'P':
                total_credit_points += credit * grade_map[grade]
                total_credits += credit
        except:
            break

    if total_credits == 0:
        return 0.0
    else:
        return total_credit_points / total_credits

# 전공평점을 계산하고 결과를 출력
result = calculate_grade_point_average()
print(f"{result:.6f}")
