def find_nth_end_number(n):
    count = 0  # 종말의 수를 찾은 개수
    number = 666  # 첫 번째 종말의 수

    while True:
        # 현재 숫자에 "666"이 포함되어 있는지 확인
        if "666" in str(number):
            count += 1
            # N번째 종말의 수를 찾으면 반환
            if count == n:
                return number
        # 다음 숫자로 이동
        number += 1

# 입력 받기
n = int(input())
# 결과 출력
print(find_nth_end_number(n))
