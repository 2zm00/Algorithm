def count_digit(start, end, digit):
    count = 0
    # 범위 내의 모든 숫자를 순회
    for num in range(start, end + 1):
        # 현재 숫자를 문자열로 변환
        num_str = str(num)
        # 문자열에서 찾고자 하는 숫자의 개수를 세어 더함
        count += num_str.count(str(digit))
    return count

# 입력 받기
start, end, digit = map(int, input().split())

# 결과 출력
result = count_digit(start, end, digit)
print(result)
