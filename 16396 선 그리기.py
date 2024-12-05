n = int(input())
lines = []

for _ in range(n):
    start, end = map(int, input().split())
    lines.append((start, 1))  # 시작점
    lines.append((end, -1))   # 끝점

lines.sort()  # 좌표를 기준으로 정렬

total_length = 0
current = 0
prev = 0

for point, change in lines:
    if current > 0:
        total_length += point - prev
    current += change
    prev = point

print(total_length)