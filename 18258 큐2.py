import sys
from collections import deque

# 명령의 수 N 입력 받기
n = int(sys.stdin.readline())

# deque 객체 생성 (큐로 사용)
queue = deque()

# N개의 명령 처리
for _ in range(n):
    # 명령 한 줄 읽고 공백 기준으로 나누기
    command_line = sys.stdin.readline().split()
    command = command_line[0]

    # push 명령 처리
    if command == "push":
        value = int(command_line[1])
        queue.append(value) # deque의 append는 O(1)

    # pop 명령 처리
    elif command == "pop":
        if not queue: # 큐가 비어있는 경우
            print(-1)
        else:
            # deque의 popleft는 O(1)
            print(queue.popleft())

    # size 명령 처리
    elif command == "size":
        print(len(queue)) # len()은 O(1)

    # empty 명령 처리
    elif command == "empty":
        # 큐가 비어있으면 True -> 1, 아니면 False -> 0
        print(1 if not queue else 0)

    # front 명령 처리
    elif command == "front":
        if not queue: # 큐가 비어있는 경우
            print(-1)
        else:
            # deque는 인덱싱으로 첫 요소 접근 가능 (O(1))
            print(queue[0])

    # back 명령 처리
    elif command == "back":
        if not queue: # 큐가 비어있는 경우
            print(-1)
        else:
            # deque는 인덱싱으로 마지막 요소 접근 가능 (O(1))
            print(queue[-1])

