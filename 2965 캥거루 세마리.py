a, b, c = map(int, input().split())
count = 0

while True:
    diff_left = b - a - 1
    diff_right = c - b - 1

    if diff_left == 0 and diff_right == 0:
        break

    if diff_left > diff_right:
        c = b
        b = a + 1
        a = a
    else:
        a = b
        b = c - 1
        c = c
    
    a, b, c = sorted([a, b, c])
    count += 1

print(count)
