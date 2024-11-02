# 줄의 수 N 입력받기
N = int(input())

# N개의 줄을 입력받아 줄 번호와 함께 출력
for i in range(1, N+1):
    line = input()
    print(f"{i}. {line}")
