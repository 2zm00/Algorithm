import sys

def get_sign(total):
    if total > 0:
        return '+'
    elif total < 0:
        return '-'
    return '0'

input = sys.stdin.readline
for _ in range(3):
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    print(get_sign(total))
