
T = int(input())  # 테스트 케이스의 개수 입력

for _ in range(T):
    string = input()  # 문자열 입력
    print(string[0] + string[-1])  