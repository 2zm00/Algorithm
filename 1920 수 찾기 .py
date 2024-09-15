
import sys

n = int(sys.stdin.readline())
# a의 갯수 입력받기
alist = set(map(int, sys.stdin.readline().split()))
# a에 대한 리스트 생성 및 a리스트에 숫자들 넣기

m = int(sys.stdin.readline())
# a와 비교할 숫자들의 갯수 입력받기
ifalist = list(map(int, sys.stdin.readline().split()))
# a와 비교당할 숫자들 리스트 생성 및 숫자들 넣기

# 비교하는 함수 생성
for num in ifalist:
    if num in alist:
        print(1)
    else:
        print(0)
