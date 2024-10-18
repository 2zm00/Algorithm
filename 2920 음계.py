def determine_scale_order(notes):
    ascending = [1, 2, 3, 4, 5, 6, 7, 8]
    descending = [8, 7, 6, 5, 4, 3, 2, 1]
    if notes == ascending:
        return 'ascending'
    elif notes == descending:
        return 'descending'
    else:
        return 'mixed'

# 사용자로부터 입력 받기
notes = list(map(int, input().split()))

# 결과 계산 및 출력
result = determine_scale_order(notes)
print(result)