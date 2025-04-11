import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 명령의 수 N 입력 받기
n = int(input())

# 정수를 저장할 스택 (파이썬 리스트 사용)
stack = []

# N번의 명령 처리
for _ in range(n):
    # 명령 한 줄 읽고 공백 기준으로 나누기
    command_line = input().split()
    command = int(command_line[0]) # 첫 번째 요소는 명령 번호

    # 1번 명령: Push X
    if command == 1:
        value = int(command_line[1]) # 두 번째 요소는 정수 X
        stack.append(value)

    # 2번 명령: Pop
    elif command == 2:
        if stack: # 스택이 비어있지 않으면
            print(stack.pop())
        else: # 스택이 비어있으면
            print(-1)

    # 3번 명령: Size
    elif command == 3:
        print(len(stack))

    # 4번 명령: IsEmpty
    elif command == 4:
        if not stack: # 스택이 비어있으면 (len(stack) == 0 과 동일)
            print(1)
        else: # 스택이 비어있지 않으면
            print(0)
        # 더 간결하게: print(1 if not stack else 0) 또는 print(int(not stack))

    # 5번 명령: Top/Peek
    elif command == 5:
        if stack: # 스택이 비어있지 않으면
            print(stack[-1]) # 맨 위 요소 출력 (제거하지 않음)
        else: # 스택이 비어있으면
            print(-1)

