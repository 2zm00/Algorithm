T = int(input())  # 테스트 케이스의 개수 입력

for _ in range(T):
    a, b = map(int, input().split(','))  # 콤마로 구분된 두 수를 입력받음
    print(a + b)
