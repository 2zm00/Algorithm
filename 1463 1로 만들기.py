import sys






def calc(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = n // 3
        else:
            n = n - 1
        count += 1
    return count


n = int(sys.stdin.readline())
result=calc(n)


print(result)