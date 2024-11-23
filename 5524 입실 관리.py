def convert_to_lowercase(N, names):
    return [name.lower() for name in names]

# 입력 받기
N = int(input())
names = []
for _ in range(N):
    names.append(input())

# 소문자로 변환하고 출력
result = convert_to_lowercase(N, names)
for name in result:
    print(name)