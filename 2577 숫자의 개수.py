A = int(input())
B = int(input())
C = int(input())

result = A * B * C

# 결과를 문자열로 변환하여 각 숫자의 개수를 세기 위해 count 함수 사용
result_str = str(result)

# 0부터 9까지의 숫자가 각각 몇 번 쓰였는지 저장할 리스트 생성
count_list = [0] * 10

# 각 숫자의 개수 세기
for digit in result_str:
    count_list[int(digit)] += 1

# 결과 출력
for count in count_list:
    print(count)