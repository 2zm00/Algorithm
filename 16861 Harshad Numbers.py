n = int(input())

def is_harshad(num):
    s = 0
    temp = num
    while temp > 0:
        s += temp % 10
        temp = temp // 10
    return num % s == 0

while True:
    if is_harshad(n):
        print(n)
        break
    n += 1
