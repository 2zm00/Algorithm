n = int(input())
que = []

for _ in range(n):
    order = input().split()
    
    if order[0] == "push":
        que.append(int(order[1]))
    elif order[0] == "pop":
        if len(que) < 1:
            print(-1)
        else:
            print(que.pop(0))
    elif order[0] == "size":
        print(len(que))
    elif order[0] == "empty":
        print(1 if len(que) < 1 else 0)
    elif order[0] == "front":
        print(-1 if len(que) < 1 else que[0])
    elif order[0] == "back":
        print(-1 if len(que) < 1 else que[-1])