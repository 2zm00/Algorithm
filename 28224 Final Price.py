n = int(input())
initial = int(input())
changes = [int(input()) for _ in range(n-1)]
print(initial + sum(changes))
